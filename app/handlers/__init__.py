from aiogram import Router, types
from aiogram.filters import Command

from app.config import config

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    text = "Привет! Я бот для уведомлений о событиях GitHub.\n\n"
    text += "Настроенные параметры:\n"
    text += f"- Owner: {config.github_owner or 'не настроен'}\n"
    text += f"- Repo: {config.github_repo or 'не настроен'}\n"
    text += f"- Интервал опроса: {config.polling_interval} сек\n"
    await message.answer(text)


@router.message(Command("status"))
async def cmd_status(message: types.Message) -> None:
    await message.answer("Бот работает!")


@router.message(Command("webhooks"))
async def cmd_webhooks(message: types.Message) -> None:
    await message.answer("Вебхук-эндпоинт: POST /webhook")