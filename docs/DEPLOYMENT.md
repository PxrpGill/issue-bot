# 🚀 Руководство по развертыванию

## Быстрый старт

### 1. Клонирование и настройка

```bash
git clone <repository-url>
cd issue-bot
cp .env.example .env
```

### 2. Заполнение переменных окружения

См. [TOKENS.md](TOKENS.md) для подробной инструкции по получению токенов.

### 3. Запуск через Docker (рекомендуется)

```bash
cd docker
docker-compose up -d
```

### 4. Запуск локально (без Docker)

```bash
# Активация виртуального окружения
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt

# Запуск
python -m app.main
```

## Требования

- Python 3.11+
- Docker & Docker Compose
- Telegram Bot Token
- GitHub App credentials
- Домен с HTTPS (для вебхуков)

## Структура сервисов

```
┌─────────────────────────────────────────────────────┐
│                   Nginx (80/443)                   │
│    /webhook → Python app (Telegram webhooks)      │
│    /health  → Health check                         │
└─────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────┐
│               Python App (aiogram + aiohttp)       │
│   - GitHub polling (issues events)                │
│   - Telegram notifications                         │
└─────────────────────────────────────────────────────┘
```

## Проверка работы

```bash
# Проверка здоровья
curl http://localhost:8080/health

# Через Docker
curl http://localhost/health
```

## Обновление

```bash
git pull
docker-compose build
docker-compose up -d
```

## Мониторинг

```bash
# Просмотр логов
docker-compose logs -f main

# Статус контейнеров
docker-compose ps
```
