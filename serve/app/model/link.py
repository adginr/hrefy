from app.db import Base
from app.helpers.date import get_expires_dt
from app.settings import settings
from sqlalchemy import Boolean, Column, DateTime, Integer, String

# from sqlalchemy.orm import relationship


class Link(Base):
    """Link class represents table columns in database"""

    id = Column(Integer, primary_key=True)
    link_short = Column(String(10), unique=True)
    link_origin = Column(String(255))
    is_active = Column(Boolean, default=True)
    expires_dt = Column(
        DateTime,
        default=lambda: get_expires_dt(days=settings.LINK_EXPIRIES_DAYS_DEFAULT),
    )  # now + 90 days
    _is_removed = Column(Boolean, default=False)

    # last_visit_dt = Column(DateTime) TODO When(dt) link was visited last time
    # fk_user_id: TODO Relate link to particular user

    def __repr__(self):
        return f"<{type(self).__name__} short link: {self.link_short}>"
