from fastapi import APIRouter

router = APIRouter()


@router.get("/users/", tags=["routers"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]