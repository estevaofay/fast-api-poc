from fastapi import FastAPI
from fastapi.testclient import TestClient


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello TikTok!"}


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello Tiktok!"}