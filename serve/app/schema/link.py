from datetime import datetime

from pydantic import BaseModel


class BaseLink(BaseModel):
    full_url: str
    expires_dt: datetime

class CreateLink(BaseLink):
    full_url: str
    fk_user_id: int

class UpdateLink(BaseLink):
    full_url: str
    expires_dt: datetime

class DbLink(BaseLink):
    id: int
    short: str
