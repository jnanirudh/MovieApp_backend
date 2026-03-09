from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 43200

    TMDB_API_KEY: str
    TMDB_BASE_URL: str = "https://api.themoviedb.org/3"

    ENVIRONMENT: str = "development"
    DEBUG: bool = True 

    model_config = {"env_file": ".env"}


settings = Settings()