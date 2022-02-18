from app.api.v1.endpoints.link import router as link_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(link_router, prefix="/link", tags=["link"])
