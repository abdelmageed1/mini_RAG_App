from pydantic_settings import BaseSettings , SettingsConfigDict # type: ignore
from typing import ClassVar

class Settings(BaseSettings):
    APP_NAME :str
    APP_VERSION :str
    Google_API_KEY:str

    FILE_ALLOWED_UPLOAD: list
    FILE_MAX_LENGHT: ClassVar[int] = 10 


    class Config():
       env_file = "res/.env"
       extra = "ignore" 


def getSetting():
    return Settings()