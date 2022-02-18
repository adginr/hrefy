# Dependencies for route

from typing import Iterator

from app.db import SessionLocal
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session


def gen_session() -> Iterator[Session]:
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except IntegrityError:
        session.rollback()
    finally:
        session.close()
