import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import dotenv_values

config = {
    **dotenv_values(".env"),
    **dotenv_values(".env.local"),
    **os.environ,  # override loaded values with environment variables
}


class Settings(BaseSettings):

    API_TELEGRAM_KEY: str | None = config.get("API_TELEGRAM_KEY")
    API_LLM_KEY: str | None = config.get("API_LLM_KEY")
    ADMIN_KEY: int | None = config.get("ADMIN_KEY")

    model_config = SettingsConfigDict()


settings = Settings()
