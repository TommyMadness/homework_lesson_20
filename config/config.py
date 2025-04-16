# config/config.py
from pydantic import BaseSettings
from dotenv import load_dotenv
from pathlib import Path
import os

CONTEXT = os.getenv("CONTEXT", "local_emulator")
load_dotenv(dotenv_path=Path(f".env.{CONTEXT}"))
load_dotenv(dotenv_path=".env.credentials", override=True)

class Config(BaseSettings):
    platformName: str
    deviceName: str
    app: str
    remote_url: str
    appWaitActivity: str = "*"
    platformVersion: str | None = None

class Credentials(BaseSettings):
    BSTACK_USERNAME: str
    BSTACK_ACCESS_KEY: str

config = Config()
credentials = Credentials()
