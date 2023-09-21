from fastapi.testclient import TestClient
from src.main import app

def test_signup(httpx_mock):
    httpx_mock.add_response(status_code=201)
    client = TestClient(app)
    response = client.post("/signup", json={"discord_id": "1234", "name": "test", "password": "test", "email": "test", "invoice": "test"})
    assert response.status_code == 201

