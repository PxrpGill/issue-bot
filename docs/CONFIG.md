# ⚙️ Конфигурация

## Все переменные окружения

| Переменная | Обязательно | Описание | Пример |
|------------|-------------|----------|--------|
| `BOT_TOKEN` | ✅ | Токен Telegram бота | `123456:ABC-DEF...` |
| `TELEGRAM_CHAT_ID` | ✅ | ID чата для уведомлений | `123456789` |
| `WEBHOOK_URL` | ❌ | URL вебхука | `https://domain.com/webhook` |
| `HOST` | ❌ | Хост для aiohttp | `0.0.0.0` |
| `PORT` | ❌ | Порт приложения | `8080` |
| `SECRET_TOKEN` | ❌ | Секрет для вебхука | `my_secret_token` |
| `GITHUB_APP_ID` | ✅ | ID GitHub App | `123456` |
| `GITHUB_APP_PRIVATE_KEY` | ✅ | Приватный ключ (PEM) | `-----BEGIN RSA...` |
| `GITHUB_INSTALLATION_ID` | ✅ | ID установки App | `12345678` |
| `GITHUB_WEBHOOK_SECRET` | ❌ | Секрет вебхука GitHub | `secret_string` |
| `GITHUB_OWNER` | ✅ | Владелец репозитория | `username` |
| `GITHUB_REPO` | ✅ | Название репозитория | `my-repo` |
| `POLLING_INTERVAL` | ❌ | Интервал опроса (сек) | `60` |

## Значения по умолчанию

```python
HOST = "0.0.0.0"
PORT = 8080
SECRET_TOKEN = ""
GITHUB_APP_ID = 0
GITHUB_APP_PRIVATE_KEY = ""
GITHUB_WEBHOOK_SECRET = ""
GITHUB_INSTALLATION_ID = 0
GITHUB_OWNER = ""
GITHUB_REPO = ""
TELEGRAM_CHAT_ID = 0
POLLING_INTERVAL = 60
```

## Пример .env

```env
# Telegram
BOT_TOKEN=123456789:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw
TELEGRAM_CHAT_ID=123456789
WEBHOOK_URL=https://your-domain.com/webhook

# Опционально
HOST=0.0.0.0
PORT=8080
SECRET_TOKEN=your_secret_token

# GitHub App (обязательно для polling)
GITHUB_APP_ID=123456
GITHUB_APP_PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAw5r...
-----END RSA PRIVATE KEY-----"
GITHUB_INSTALLATION_ID=12345678
GITHUB_WEBHOOK_SECRET=github_webhook_secret

# GitHub Repository
GITHUB_OWNER=your_username
GITHUB_REPO=your_repository

# Настройки
POLLING_INTERVAL=60
```

## Загрузка конфигурации

Конфигурация загружается из `.env` файла через Pydantic Settings:

```python
from app.config import config

print(config.bot_token)
print(config.github_owner)
```
