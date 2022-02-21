from app import crud, schema
from app.api.deps import gen_session
from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm.session import Session

router = APIRouter()


@router.post("/", response_model=schema.DBLink, status_code=status.HTTP_201_CREATED)
def create(obj_in: schema.CreateLink, session: Session = Depends(gen_session)):
    obj_db = crud.link.create(obj_in, session)
    return obj_db


@router.get("/redirect/{link_short:str}", response_class=RedirectResponse)
def redirect(link_short: str, session: Session = Depends(gen_session)):
    db_obj = crud.link.read(session, link_short)
    if db_obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return db_obj.link_origin


@router.get("/{link_short:str}", response_model=schema.DBLink)
def read(link_short: str, session: Session = Depends(gen_session)):
    db_obj = crud.link.read(session, link_short)
    if db_obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return db_obj


@router.get("/", response_model=list[schema.DBLink])
def get_all(session: Session = Depends(gen_session)):
    return crud.link.get_all(session)


@router.put(
    "/{link_short}", status_code=status.HTTP_200_OK, response_model=schema.DBLink
)
def update_link(
    obj_in: schema.UpdateLink, link_short: str, session: Session = Depends(gen_session)
):
    db_obj = crud.link.read(session, link_short)
    if db_obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    # Vefiry wether new link_short is unique
    is_link_short_passed = obj_in.dict().get("link_short")
    if is_link_short_passed is not None and is_link_short_passed != link_short:
        check_db_obj = crud.link.read(session, is_link_short_passed)
        if check_db_obj is not None:
            raise HTTPException(
                status.HTTP_409_CONFLICT, f"Short link <{link_short}> already exists"
            )

    # Update entity
    db_obj = crud.link.update(session, obj_in, db_obj)
    return db_obj


@router.delete("/{link_short:str}", status_code=status.HTTP_202_ACCEPTED)
def delete(link_short: str, session: Session = Depends(gen_session)):
    db_obj = crud.link.delete(session, link_short)
    if db_obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"detail": "Removed"}
