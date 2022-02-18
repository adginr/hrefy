from app.settings import settings
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

engine = create_engine(f"sqlite:///{settings.DB_PATH}", future=True)
SessionLocal = sessionmaker(bind=engine)
