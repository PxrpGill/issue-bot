# Telegram Bot Project

## Описание
Telegram-бот с вебхуками на aiogram 3.x + aiohttp.

## Стек
- Python 3.10+
- aiogram 3.4.1
- aiohttp 3.9.3
- pydantic 2.5.3

## Структура
```
app/
├── main.py          # Точка входа
├── config.py        # Конфиг (Pydantic Settings)
├── webhooks.py     # Вебхук-эндпоинты
├── handlers/       # Обработчики
├── middlewares/    # Мидлвары
├── keyboards/      # Клавиатуры
├── services/      # Бизнес-логика
└── models/        # Модели
```

## Переменные окружения
- BOT_TOKEN — токен бота
- WEBHOOK_URL — URL для вебхука
- HOST — хост (по умолчанию 0.0.0.0)
- PORT — порт (по умолчанию 8080)
- SECRET_TOKEN — секретный токен для вебхука

## Запуск
```bash
python -m app.main
```

## Эндпоинты
- GET /health — health check
- POST /webhook — webhook handler
