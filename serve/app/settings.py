import pathlib
from dataclasses import dataclass

APP_DIR = pathlib.Path(__file__).parent


@dataclass
class Settings:
    DB_PATH = APP_DIR / "db.sqlite3"
    DEFAULT_LINK_EXPIRIES_DAYS:int = 90


settings = Settings()
