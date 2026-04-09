# GitHub Issue Bot

Telegram-бот для уведомлений о событиях GitHub через GitHub App и polling.

## Возможности

- Оповещения об открытии/закрытии issues и PR
- Уведомления о метках (labels)
- Оповещения о назначении исполнителей (assignees)
- Уведомления о milestone
- Поддержка project board (перемещение колонок)

## Структура проекта

```
project/
├── app/
│   ├── main.py              # Точка входа (aiohttp)
│   ├── config.py            # Конфигурация (Pydantic)
│   ├── webhooks.py          # Обработка вебхуков
│   ├── handlers/            # Обработчики сообщений
│   ├── middlewares/         # Промежуточное ПО
│   ├── services/
│   │   ├── github_poller.py # GitHub API polling
│   │   └── notifications.py # Уведомления
│   └── models/
│       └── github.py        # Модели GitHub
├── .env.example             # Пример конфига
├── requirements.txt         # Зависимости
└── README.md
```

## Установка

```bash
# Копирование конфига
cp .env.example .env

# Установка зависимостей
pip install -r requirements.txt
```

## Настройка .env

```env
# Telegram
BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id
WEBHOOK_URL=https://your-domain.com/webhook
HOST=0.0.0.0
PORT=8080
SECRET_TOKEN=your_secret_token_here

# GitHub App
GITHUB_APP_ID=123456
GITHUB_APP_PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----\n..."
GITHUB_INSTALLATION_ID=789012
GITHUB_OWNER=your_owner
GITHUB_REPO=your_repo
POLLING_INTERVAL=60
```

## Настройка GitHub App

1. Создать GitHub App на https://github.com/settings/apps
2. Настроить permissions:
   - `issues`: Read-only
   - `metadata`: Read-only
3. Установить App в репозиторий
4. Скопировать параметры в `.env`:
   - `GITHUB_APP_ID` — App ID
   - `GITHUB_APP_PRIVATE_KEY` — приватный ключ (.pem файл)
   - `GITHUB_INSTALLATION_ID` — ID установки (из URL после установки)

## Запуск

```bash
python -m app.main
```

## Эндпоинты

- `GET /health` — проверка здоровья
- `POST /webhook` — вебхук от Telegram

## Стек

- aiogram 3.x — Telegram API
- aiohttp — веб-сервер
- Pydantic — валидация конфигурации
- PyJWT — работа с GitHub App JWT