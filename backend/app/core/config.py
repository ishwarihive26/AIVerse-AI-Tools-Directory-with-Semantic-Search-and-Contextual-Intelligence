"""
This file reads values from the .env file and makes them available
to the rest of the app as a single `settings` object.
Instead of writing os.getenv("DATABASE_URL") everywhere, we write
settings.DATABASE_URL - safer and has autocomplete.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str = "dev-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080

    CLOUDINARY_CLOUD_NAME: str = ""
    CLOUDINARY_API_KEY: str = ""
    CLOUDINARY_API_SECRET: str = ""

    FRONTEND_URL: str = "http://localhost:3000"

    class Config:
        env_file = ".env"


# Import this single instance anywhere you need config values
settings = Settings()
