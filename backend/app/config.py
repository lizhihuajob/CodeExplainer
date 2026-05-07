from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/codeexplain"

    class Config:
        env_file = ".env"


settings = Settings()
