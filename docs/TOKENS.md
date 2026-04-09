# 🔑 Получение токенов и учетных данных

## Telegram Bot Token

### Где получить

1. Откройте @BotFather в Telegram
2. Отправьте `/newbot` для создания нового бота
3. Следуйте инструкциям, назовите бота
4. Скопируйте токен вида `1234567890:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw`

### Переменная

```
BOT_TOKEN=1234567890:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw
```

## Telegram Chat ID

### Где получить

1. Добавьте бота в чат/канал
2. Перешлите любое сообщение боту @userinfobot
3. Бот покажет ваш chat_id

### Переменная

```
TELEGRAM_CHAT_ID=123456789
```

## Telegram Webhook Secret (опционально)

### Зачем нужен

Защита вебхука от несанкционированных запросов. Любую строку.

### Переменная

```
SECRET_TOKEN=your_secret_token_here
```

## GitHub App Credentials

### Шаг 1: Создание GitHub App

1. Перейдите https://github.com/settings/apps/new
2. Заполните:
   - **Name**: Issue Bot (或者 другое имя)
   - **Homepage URL**: `https://your-domain.com`
   - **Webhook URL**: `https://your-domain.com/webhook`
   - **Webhook secret**: generated or custom string

### Шаг 2: Настройка Permissions

Перейдите в "Permissions" и настройте:

| Permission | Access |
|------------|--------|
| Issues     | Read-only |
| Metadata   | Read-only |

### Шаг 3: Подписка на события

Перейдите в "Subscribe to events" и выберите:
- ☐ Issues
- ☐ Issue comment

### Шаг 4: Установка App

1. Нажмите "Install" (зеленая кнопка)
2. Выберите репозитории
3. СкопируйтеInstallation ID из URL:

```
https://github.com/settings/installations/12345678
                                      ^^^^^^^^
                                GITHUB_INSTALLATION_ID
```

### Шаг 5: Приватный ключ

1. В GitHub App странице нажмите "Generate a private key"
2. Скачается файл `.pem`
3. Содержимое файла — это `GITHUB_APP_PRIVATE_KEY`

### Переменные

```
GITHUB_APP_ID=123456
GITHUB_APP_PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----
...
-----END RSA PRIVATE KEY-----"
GITHUB_INSTALLATION_ID=12345678
GITHUB_WEBHOOK_SECRET=your_webhook_secret
```

## GitHub Owner и Repo

### Owner

Имя пользователя или организации на GitHub.

### Repo

Наименование репозитория.

### Переменные

```
GITHUB_OWNER=your_username
GITHUB_REPO=your_repository
```

## Итоговый .env файл

```env
# Telegram
BOT_TOKEN=1234567890:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw
TELEGRAM_CHAT_ID=123456789
WEBHOOK_URL=https://your-domain.com/webhook
SECRET_TOKEN=your_secret_token

# GitHub
GITHUB_APP_ID=123456
GITHUB_APP_PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----
your private key content here
-----END RSA PRIVATE KEY-----"
GITHUB_INSTALLATION_ID=12345678
GITHUB_WEBHOOK_SECRET=your_webhook_secret
GITHUB_OWNER=your_username
GITHUB_REPO=your_repository

# Настройки
POLLING_INTERVAL=60
```
