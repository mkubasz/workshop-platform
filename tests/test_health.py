import pytest
from fastapi.testclient import TestClient

from src.main import app


def test_healthz():
    client = TestClient(app)
    response = client.get("/healthz")
    assert response.status_code == 200
