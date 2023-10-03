import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core.config import ApiConfig, TestApiConfig
from src.database import connection, Base
from src.main import get_application


@pytest.fixture
def api_config() -> ApiConfig:
    return TestApiConfig()


@pytest.fixture
def fastapi_app(api_config: ApiConfig) -> FastAPI:
    return get_application(config=api_config)


async def test_connection():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    with SessionLocal() as session:
        yield session


@pytest.fixture
def client(fastapi_app: FastAPI) -> TestClient:
    fastapi_app.dependency_overrides[connection] = test_connection
    return TestClient(app=fastapi_app)
