from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
  """
  Application settings using Pydantic for configuration management.
  """
  APP_NAME: str = "My Application"
  APP_ENV: str = "local"
  PORT: int = 8000
  DEBUG: bool = False
  APP_WORKERS: int = 1

  class Config:
    env_file = BASE_DIR / ".env"
    env_file_encoding = "utf-8"

settings = Settings()
