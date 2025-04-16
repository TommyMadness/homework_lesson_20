from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    browserstack_username: str
    browserstack_access_key: str
    browserstack_url: str
    app_url: str

    android_device_name: str
    android_os_version: str

    ios_device_name: str
    ios_os_version: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
