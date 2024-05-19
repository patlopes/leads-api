from pydantic_settings import BaseSettings

class Config(BaseSettings):
    """
    This class will automatically load the environment variables from the system
    """
    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str