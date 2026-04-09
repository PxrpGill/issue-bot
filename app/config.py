from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: str
    webhook_url: str
    host: str = "0.0.0.0"
    port: int = 8080
    secret_token: str = ""

    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache
def get_settings() -> Settings:
    return Settings()


config = get_settings()