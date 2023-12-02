from fastapi import APIRouter

from .endpoints import users, items

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(items.router, prefix="/items", tags=["Items"])