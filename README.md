# Telegram Bot with Webhooks

Python Telegram-бот с вебхуками на aiogram 3.x.

## Структура проекта

```
project/
├── app/
│   ├── __init__.py
│   ├── main.py          # Точка входа (aiohttp)
│   ├── config.py        # Конфигурация (Pydantic)
│   ├── webhooks.py     # Обработка вебхуков
│   ├── handlers/        # Обработчики сообщений
│   ├── middlewares/     # Промежуточное ПО
│   ├── keyboards/       # Клавиатуры
│   ├── services/       # Бизнес-логика
│   └── models/         # Модели данных
├── .env.example        # Пример конфига
├── requirements.txt    # Зависимости
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
BOT_TOKEN=your_bot_token_here
WEBHOOK_URL=https://your-domain.com/webhook
HOST=0.0.0.0
PORT=8080
SECRET_TOKEN=your_secret_token_here
```

## Запуск

```bash
# Локально
python -m app.main

# Docker
docker-compose up --build
```

## Эндпоинты

- `GET /health` — проверка здоровья
- `POST /webhook` — вебхук от Telegram

## Разработка

- aiogram 3.x — основной фреймворк
- aiohttp — веб-сервер
- Pydantic — валидация конфигурации
