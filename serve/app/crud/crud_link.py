from app import model, schema
from app.helpers.encode import num_encode
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, update
from sqlalchemy.orm.session import Session

from .crud_base import CRUDBase


class CRUDLink(CRUDBase[model.Link, schema.CreateLink, schema.UpdateLink]):
    def create(self, obj_in: schema.CreateLink, session: Session) -> model.Link:
        new_obj = model.Link(**obj_in.dict())
        session.add(new_obj)
        session.flush()
        id: int = new_obj.id
        setattr(new_obj, "link_short", num_encode(id))
        session.add(new_obj)
        session.commit()
        return new_obj

    def read(self, session: Session, link_short: str) -> model.Link | None:
        """a.k.a. Get link by link_short"""
        stmt = (
            select(self.model)
            .where(self.model.link_short == link_short)
            .where(self.model._is_removed == False)
        )
        return session.execute(stmt).scalar_one_or_none()

    def update(self, session: Session, obj_in: schema.UpdateLink, db_obj: model.Link):
        json_obj = obj_in.dict(exclude_defaults=True, exclude_none=True)
        for field in json_obj:
            setattr(db_obj, field, json_obj[field])
        session.add(db_obj)
        session.commit()
        return db_obj

    def delete(self, session: Session, link_short: str) -> model.Link | None:
        # Update
        update_stmt = (
            update(self.model)
            .where(self.model.link_short == link_short)
            .values(_is_removed=True)
        )
        session.execute(update_stmt)

        # Select
        select_stmt = select(self.model).where(self.model.link_short == link_short)
        return session.execute(select_stmt).scalar_one_or_none()

    def get_all(self, session: Session):
        stmt = select(self.model).where(self.model._is_removed != True)
        return [obj[0] for obj in session.execute(stmt).fetchall()]


crud_link = CRUDLink(model.Link)  # type: ignore
