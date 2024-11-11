from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Configuration(BaseSettings):
    TELEGRAM_BOT_TOKEN: SecretStr
    DATABASE_URL: SecretStr
    ADMIN_ID: int
    
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )

BotSettings = Configuration()
