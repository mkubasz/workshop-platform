import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.api.config import ApiConfig, TestApiConfig
from src.main import get_application

@pytest.fixture
def api_config() -> ApiConfig:
    return TestApiConfig()

@pytest.fixture
def fastapi_app(api_config: ApiConfig) -> FastAPI:
    return get_application(config=api_config)

@pytest.fixture
def client(fastapi_app: FastAPI) -> TestClient:
    return TestClient(app=fastapi_app)
