from app.db import Base
from sqlalchemy import Boolean, Column, DateTime, Integer, String

# from sqlalchemy.orm import relationship


class Link(Base):
    """Link class represents table columns in database"""

    id = Column(Integer, primary_key=True)
    link_short = Column(String(10), unique=True)
    link_full = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
    expiries_dt = Column(DateTime)  # now + 90 days

    # last_visit_dt = Column(DateTime) TODO When(dt) link was visited last time
    # fk_user_id: TODO Relate link to particular user

    def __repr__(self):
        return f"<{type(self).__name__} short link: {self.link_short}>"
