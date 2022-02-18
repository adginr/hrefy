import typing as ty

from app.db import Base
from pydantic import BaseModel
from sqlalchemy.orm.session import Session

ModelType = ty.TypeVar("ModelType", bound=Base)
CreateSchemaType = ty.TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = ty.TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(ty.Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """Base class exposes methods for [C]reate, [R]ead, [U]pdate, [D]elete data"""

    def __init__(self, model: ModelType):
        self.model = model

    def create(self, obj_in: CreateSchemaType, session: Session) -> ty.Any:
        pass
