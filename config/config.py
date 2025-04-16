from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
import os

CONTEXT = os.getenv("CONTEXT", "local_emulator")

# Подгружаем переменные вручную
load_dotenv(dotenv_path=Path(f".env.{CONTEXT}"))
load_dotenv(dotenv_path=".env.credentials", override=True)

class Config(BaseSettings):
    platformName: str = Field(..., env="PLATFORM_NAME")
    deviceName: str = Field(..., env="DEVICE_NAME")
    app: str = Field(..., env="APP")
    remote_url: str = Field(..., env="REMOTE_URL")
    appWaitActivity: str = Field("*", env="APP_WAIT_ACTIVITY")
    platformVersion: str | None = Field(None, env="PLATFORM_VERSION")

    model_config = SettingsConfigDict(
        env_file=None,  # отключаем повторную загрузку
        extra="allow"   # допускаем лишние переменные (если они есть в os.environ)
    )

class Credentials(BaseSettings):
    BSTACK_USERNAME: str = Field(..., env="BSTACK_USERNAME")
    BSTACK_ACCESS_KEY: str = Field(..., env="BSTACK_ACCESS_KEY")

    model_config = SettingsConfigDict(
        env_file=".env.credentials",
        env_file_encoding="utf-8"
    )

config = Config()
credentials = Credentials()
