from fastapi import FastAPI

from .routers import users

app = FastAPI()

app.include_router(users.router)

@app.get("/")
async def get():
    return {"message": "Hello TikTok!"}


