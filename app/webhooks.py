from aiohttp import web

from app.config import config


def setup_webhooks(app: web.Application) -> None:
    async def health_check(request: web.Request) -> web.Response:
        return web.Response(text="OK")

    async def webhook_handler(request: web.Request) -> web.Response:
        if config.secret_token:
            token = request.headers.get("X-Telegram-Bot-Api-Secret-Token")
            if token != config.secret_token:
                return web.Response(status=403, text="Forbidden")

        bot = request.app["bot"]
        dp = request.app["dispatcher"]

        update = await request.json()
        await dp.feed_webhook_update(bot, update)

        return web.Response(text="OK")

    app.router.add_get("/health", health_check)
    app.router.add_post("/webhook", webhook_handler)