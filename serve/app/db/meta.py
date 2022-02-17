from typing import Any

from sqlalchemy.ext.declarative import DeclarativeMeta, declared_attr
from sqlalchemy.orm import registry

mapper_registry = registry()


class Base(metaclass=DeclarativeMeta):
    id: Any
    __name__: str
    __abstract__ = True
    registry = mapper_registry
    metadata = mapper_registry.metadata
    __init__ = mapper_registry.constructor

    @declared_attr
    def __tablename__(cls) -> str:
        cls_name: str = getattr(cls, "__name__")
        return cls_name.lower()
