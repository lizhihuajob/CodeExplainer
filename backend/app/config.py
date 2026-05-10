from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/codeexplain"
    FRONTEND_DIR: str = ""
    DATA_SOURCE_URL: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
