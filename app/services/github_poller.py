import asyncio
import logging
from datetime import datetime, timezone
from typing import Any, Callable

import aiohttp
import jwt
from aiogram import Bot

from app.config import config

logger = logging.getLogger(__name__)


class GitHubPoller:
    def __init__(self, bot: Bot, on_event: Callable[[str, dict], None]):
        self.bot = bot
        self.on_event = on_event
        self._task: asyncio.Task | None = None
        self._running = False
        self._last_event_id: str | None = None

    async def _get_access_token(self) -> str:
        now = datetime.now(timezone.utc)
        payload = {
            "iat": now,
            "exp": now.replace(minute=now.minute + 9),
            "iss": config.github_app_id,
        }
        token = jwt.encode(
            payload,
            config.github_app_private_key,
            algorithm="RS256",
        )

        async with aiohttp.ClientSession() as session:
            url = f"https://api.github.com/app/installations/{config.github_installation_id}/access_tokens"
            async with session.post(
                url,
                headers={
                    "Authorization": f"Bearer {token}",
                    "Accept": "application/vnd.github+json",
                },
                json={"permissions": {"issues": "read", "metadata": "read"}},
            ) as resp:
                data = await resp.json()
                return data["token"]

    def _event_type(self, event: dict) -> str:
        return event.get("event", "")

    async def _fetch_events(self) -> list[dict]:
        if not config.github_owner or not config.github_repo:
            logger.warning("GitHub owner/repo not configured")
            return []

        try:
            access_token = await self._get_access_token()
        except Exception as e:
            logger.error(f"Failed to get access token: {e}")
            return []

        url = f"https://api.github.com/repos/{config.github_owner}/{config.github_repo}/issues/events"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as resp:
                if resp.status != 200:
                    logger.error(f"Failed to fetch events: {resp.status}")
                    return []
                return await resp.json()

    async def _poll(self) -> None:
        while self._running:
            try:
                events = await self._fetch_events()
                for event in reversed(events):
                    event_id = str(event.get("id", ""))
                    if self._last_event_id is None or event_id > self._last_event_id:
                        self._last_event_id = event_id
                        event_type = self._event_type(event)
                        await self.on_event(event_type, event)
            except Exception as e:
                logger.error(f"Polling error: {e}")

            await asyncio.sleep(config.polling_interval)

    async def start(self) -> None:
        self._running = True
        initial_events = await self._fetch_events()
        if initial_events:
            self._last_event_id = str(initial_events[0].get("id", ""))
        self._task = asyncio.create_task(self._poll())
        logger.info("GitHub polling started")

    async def stop(self) -> None:
        self._running = False
        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
        logger.info("GitHub polling stopped")