from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: str
    webhook_url: str
    host: str = "0.0.0.0"
    port: int = 8080
    secret_token: str = ""

    github_app_id: int = 0
    github_app_private_key: str = ""
    github_webhook_secret: str = ""
    github_installation_id: int = 0

    github_owner: str = ""
    github_repo: str = ""

    telegram_chat_id: int = 0

    polling_interval: int = 60

    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache
def get_settings() -> Settings:
    return Settings()


config = get_settings()