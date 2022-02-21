import pathlib
import string
from dataclasses import dataclass

APP_DIR = pathlib.Path(__file__).parent


@dataclass
class Settings:
    DB_PATH = APP_DIR / "db.sqlite3"
    LINK_EXPIRIES_DAYS_DEFAULT: int = 90
    LINK_EXPIRIES_DAYS_MIN: int = 1
    LINK_EXPIRIES_DAYS_MAX: int = 365

    ACCEPTABLE_ENCODE_CRARS_SET = set(string.ascii_letters + string.digits)


settings = Settings()
