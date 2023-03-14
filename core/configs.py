from pydantic import BaseSettings
from decouple import config


class Settings(BaseSettings):
    API_V1_STR: str = config('API_V1_STR')
    DB_URL: str = config('DB_URL')

    class Config:
        case_sensitive = True

settings: Settings = Settings()
