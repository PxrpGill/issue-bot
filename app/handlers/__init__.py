from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    await message.answer("Привет! Нажми /webhooks для настройки вебхуков.")


@router.message()
async def default_handler(message: types.Message) -> None:
    await message.answer("Я получил ваше сообщение!")