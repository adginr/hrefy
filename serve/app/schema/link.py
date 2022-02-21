from datetime import datetime, timedelta
from typing import Any, Callable

from app.settings import settings
from pydantic import BaseModel, HttpUrl, validator


class BaseLink(BaseModel):
    link_origin: HttpUrl
    expires_dt: datetime | None = datetime.now() + timedelta(
        days=settings.LINK_EXPIRIES_DAYS_DEFAULT
    )
    is_active: bool = True

    @validator("expires_dt")
    def check_dt_within_min_and_max(cls, v: datetime):
        tz = v.tzinfo if hasattr(v, "tzinfo") else None
        now = datetime.now(tz=tz)
        days_after_now: Callable[[int], datetime] = lambda days: (
            now + timedelta(days=days)
        )
        err_msg = f"Date should be within {days_after_now(settings.LINK_EXPIRIES_DAYS_MIN):%Y-%m-%d} and {days_after_now(settings.LINK_EXPIRIES_DAYS_MAX):%Y-%m-%d}"
        assert (
            days_after_now(settings.LINK_EXPIRIES_DAYS_MIN)
            <= v
            <= days_after_now(settings.LINK_EXPIRIES_DAYS_MAX)
        ), err_msg
        return v

    class Config:
        orm_mode = True


class CreateLink(BaseLink):
    # fk_user_id: int
    pass


class UpdateLink(BaseLink):
    link_short: str | None

    @validator("link_short")
    def check_acceptable_chars(cls, v: str):
        if not (set(v) - settings.ACCEPTABLE_ENCODE_CRARS_SET == set()):
            raise ValueError(
                f"Short must contain only: {settings.ACCEPTABLE_ENCODE_CRARS_SET}"
            )
        return v


class DBLink(BaseLink):
    id: int
    link_short: str
