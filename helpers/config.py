from pydantic_settings import BaseSettings , SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME :str
    APP_VERSIONL :str
    Google_API_KEY:str

    class config():
       env_file = '.env'


def getSetting():
    return Settings()