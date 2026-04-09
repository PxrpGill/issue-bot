import asyncio
import logging
from contextlib import asynccontextmanager

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiohttp import web

from app.config import config
from app.handlers import router as handlers_router
from app.middlewares import setup_middlewares
from app.services.github_poller import GitHubPoller
from app.services.notifications import send_notification
from app.webhooks import setup_webhooks


async def on_github_event(event_type: str, event: dict, bot: Bot) -> None:
    await send_notification(bot, event_type, event)


async def on_startup(bot: Bot) -> None:
    if config.webhook_url:
        await bot.set_webhook(
            url=config.webhook_url,
            drop_pending_updates=True,
        )
    poller = GitHubPoller(bot, lambda et, ev: on_github_event(et, ev, bot))
    await poller.start()
    bot["github_poller"] = poller


async def on_shutdown(bot: Bot) -> None:
    poller = bot.get("github_poller")
    if poller:
        await poller.stop()
    await bot.delete_webhook()


@asynccontextmanager
async def lifespan(app: web.Application):
    bot = app["bot"]
    await on_startup(bot)
    yield
    await on_shutdown(bot)


async def create_app() -> web.Application:
    bot = Bot(
        token=config.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    dp.include_router(handlers_router)
    setup_middlewares(dp)

    app = web.Application(lifespan=lifespan)
    app["bot"] = bot
    app["dispatcher"] = dp

    setup_webhooks(app)

    return app


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    app = asyncio.run(create_app())
    web.run_app(
        app,
        host=config.host,
        port=config.port,
    )


if __name__ == "__main__":
    main()
