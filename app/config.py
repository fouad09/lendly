from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int
    BUCKET_NAME: str
    ENV: str
    ADMIN_SECRET_KEY: str
    GOOGLE_APPLICATION_CREDENTIALS: str
    GOOGL_SHEET_RATE_ID: str
    model_config = SettingsConfigDict(env_file=".env")


def get_settings(test: bool = False):
    settings = Settings().model_dump()

    if settings["ENV"] == "Local":
        settings["DEBUG"] = True
        settings["DATABASE_URL"] = "sqlite:///lendly.db"
    else:
        settings["DEBUG"] = False
        if settings["DATABASE_URL"].startswith("postgres://"):
            settings["DATABASE_URL"] = settings["DATABASE_URL"].replace(
                "postgres://", "postgresql://", 1
            )

    if test:
        settings["IS_TESTING"] = True
    else:
        settings["IS_TESTING"] = False

    return settings


settings = get_settings()
