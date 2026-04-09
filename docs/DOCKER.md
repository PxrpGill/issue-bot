# 🐳 Docker-конфигурация

## Структура файлов

```
docker/
├── Dockerfile         # Multi-stage build Python приложения
├── docker-compose.yml # Оркестрация сервисов
├── nginx/
│   └── nginx.conf    # Nginx конфигурация
├── Makefile          # Команды для удобства
└── .env.example      # Пример переменных окружения
```

## Быстрый старт

### 1. Копирование .env

```bash
cp docker/.env.example .env
```

### 2. Запуск

```bash
cd docker
docker-compose up -d
```

### 3. Проверка

```bash
curl http://localhost/health
```

## Команды Makefile

```bash
make up        # Запуск (detached)
make down      # Остановка
make logs      # Просмотр логов
make rebuild   # Пересборка
make clean     # Очистка
```

## Конфигурация Compose

### Сервисы

| Сервис   | Порт  | Описание                    |
|----------|-------|----------------------------|
| main     | 8080  | Python приложение         |
| nginx    | 80,443| Обратный прокси            |

### Переменные окружения

```yaml
env_file:
  - .env
```

### Healthcheck

- Python app: `GET /health` через wget
- Nginx: ждёт пока main станет healthy

## Сетевые настройки

Сервисы работают в сети `app-network` (bridge driver).

```
Nginx (80/443) → main:8080
```

## Конфигурация Nginx

Прокидывает:
- `/health` → main:8080/health
- `/webhook` → main:8080/webhook

## Сборка вручную

```bash
docker build -t issue-bot -f docker/Dockerfile .
docker run -d -p 8080:8080 --env-file .env issue-bot
```

## Production-рекомендации

1. **HTTPS**: Настройте SSL/TLS сертификаты в nginx.conf
2. **Переменные**: Используйте Docker secrets или внешний .env
3. **Логирование**: Настройте ротацию логов
4. **Мониторинг**: Добавьте Prometheus metrics
