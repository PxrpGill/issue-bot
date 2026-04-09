# Telegram Bot Project

## Описание
Telegram-бот с GitHub App polling на aiogram 3.x + aiohttp.

## Стек
- Python 3.10+
- aiogram 3.4.1
- aiohttp 3.9.3
- pydantic 2.5.3
- PyJWT 2.8.0

## Структура
```
app/
├── main.py          # Точка входа
├── config.py        # Конфиг (Pydantic Settings)
├── webhooks.py      # Вебхук-эндпоинты
├── handlers/        # Обработчики
├── middlewares/     # Мидлвары
├── services/        # Бизнес-логика
│   ├── github_poller.py   # GitHub API polling
│   └── notifications.py  # Уведомления
└── models/          # Модели
    └── github.py   # GitHub модели
```

## Переменные окружения
- BOT_TOKEN — токен бота
- WEBHOOK_URL — URL для вебхука (опционально)
- HOST — хост (по умолчанию 0.0.0.0)
- PORT — порт (по умолчанию 8080)
- SECRET_TOKEN — секретный токен для вебхука
- GITHUB_APP_ID — ID GitHub App
- GITHUB_APP_PRIVATE_KEY — приватный ключ GitHub App
- GITHUB_WEBHOOK_SECRET — секрет для вебхука GitHub
- GITHUB_INSTALLATION_ID — ID установки GitHub App
- GITHUB_OWNER — владелец репозитория
- GITHUB_REPO — название репозитория
- TELEGRAM_CHAT_ID — ID чата для уведомлений
- POLLING_INTERVAL — интервал опроса в секундах (по умолчанию 60)

## Запуск
```bash
pip install -r requirements.txt
python -m app.main
```

## Эндпоинты
- GET /health — health check
- POST /webhook — webhook handler (Telegram)

## GitHub App Setup
1. Создать GitHub App на https://github.com/settings/apps
2. Настроить permissions: issues:read, metadata:read
3. Установить App в репозиторий
4. Скопировать App ID, private key, installation ID в .env
