import os

from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

@dataclass
class Settings:
    app_name: str = os.getenv(
        "APP_NAME",
        "Piccolo AI"
    )

    environment: str = os.getenv(
        "APP_ENV",
        "development"
    )

    model_name: str = os.getenv(
        "MODEL_NAME",
        "default_model"
    )

settings = Settings()