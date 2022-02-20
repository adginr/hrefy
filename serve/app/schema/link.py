from typing import Any

from pydantic import BaseModel, HttpUrl


class BaseLink(BaseModel):
    link_origin: HttpUrl
    expires_dt: Any
    is_active: bool = True


class CreateLink(BaseLink):
    # fk_user_id: int
    pass


class UpdateLink(BaseLink):
    pass


class DBLink(BaseLink):
    id: int
    link_short: str

    class Config:
        orm_mode = True
