from fastapi.testclient import TestClient

from app.config import settings
from app.main import app

client = TestClient(app)
settings.test_url = "https://testurl.com"


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'test_url': 'https://testurl.com'}
