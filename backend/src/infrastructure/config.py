from pydantic_settings import BaseSettings

class Config(BaseSettings):
    """
    This class will automatically load the environment variables from the system
    """
    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    API_MINIO_HOST: str
    MINIO_ROOT_USER: str
    MINIO_ROOT_PASSWORD: str
    MINIO_BUCKET: str
    MINIO_SECURE: bool = False
    DEFAULT_EMAIL_ADMIN: str