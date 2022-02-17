# Import all the models, so that Base has them before being
# imported by Alembic

from app.model import Link

from .meta import Base
