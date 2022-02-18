from app import crud, schema
from app.api.deps import gen_session
from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session

router = APIRouter()


@router.post("/", response_model=schema.DBLink, status_code=status.HTTP_201_CREATED)
def create(obj_in: schema.CreateLink, session: Session = Depends(gen_session)):
    obj_db = crud.link.create(obj_in, session)
    return obj_db


@router.get("/{link_short:str}", response_model=schema.DBLink)
def read(link_short: str, session: Session = Depends(gen_session)):
    db_obj = crud.link.read(session, link_short)
    if db_obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return db_obj


@router.put("/", status_code=status.HTTP_200_OK)
def update_link(obj_in: schema.UpdateLink, session: Session = Depends(gen_session)):
    db_obj = crud.link.update(session, obj_in)
    if db_obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"detail": "Removed"}


@router.delete("/{link_short:str}", status_code=status.HTTP_202_ACCEPTED)
def delete(link_short: str, session: Session = Depends(gen_session)):
    db_obj = crud.link.delete(session, link_short)
    if db_obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"detail": "Removed"}
