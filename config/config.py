from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
import os

CONTEXT = os.getenv("CONTEXT", "local_emulator")

load_dotenv(dotenv_path=Path(f".env.{CONTEXT}"))
load_dotenv(dotenv_path=".env.credentials", override=True)


class Config(BaseSettings):
    platformName: str = Field(..., alias="PLATFORM_NAME")
    appiumVersion: str | None = Field(None, alias="APPIUM_VERSION")
    deviceName: str = Field(..., alias="DEVICE_NAME")
    app: str = Field(..., alias="APP")
    remote_url: str = Field(..., alias="REMOTE_URL")
    appWaitActivity: str = Field("*", alias="APP_WAIT_ACTIVITY")
    platformVersion: str | None = Field(None, alias="PLATFORM_VERSION")

    model_config = SettingsConfigDict(env_file=None, env_parse_all=True, extra="allow")


class Credentials(BaseSettings):
    BSTACK_USERNAME: str = Field(..., alias="BSTACK_USERNAME")
    BSTACK_ACCESS_KEY: str = Field(..., alias="BSTACK_ACCESS_KEY")

    model_config = SettingsConfigDict(env_file=None, env_parse_all=True, extra="allow")


config = Config()
credentials = Credentials()
