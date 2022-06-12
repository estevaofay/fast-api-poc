import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    test_url: str = os.getenv("TEST_URL", "")


settings = Settings()
