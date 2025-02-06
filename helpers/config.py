from pydantic_settings import BaseSettings , SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME :str
    APP_VERSION :str
    Google_API_KEY:str

    class Config():
       env_file = "res/.env"


def getSetting():
    return Settings()