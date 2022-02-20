import pytest
from app.api.deps import gen_session
from app.db import Base
from app.main import app
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

DB_URL = "sqlite:///test.db"
engine = create_engine(DB_URL, future=True)
TestLocalSession = sessionmaker(engine)

# Crete DB
Base.metadata.create_all(bind=engine)


def override_gen_session():
    session = TestLocalSession()
    try:
        yield session
    except IntegrityError:
        session.rollback()
    finally:
        session.close()


app.dependency_overrides[gen_session] = override_gen_session


@pytest.fixture(scope="module")
def client():
    Base.metadata.create_all(bind=engine)
    client = TestClient(app)
    try:
        yield client
    finally:
        Base.metadata.drop_all(bind=engine)
