from fastapi import FastAPI

from .config import settings
from .routers import users, accounts

app = FastAPI()

app.include_router(users.router)
app.include_router(accounts.router)


@app.get("/")
async def get():
    return {
        "test_url": settings.test_url
    }
