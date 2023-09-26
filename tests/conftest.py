import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.core.config import ApiConfig, TestApiConfig
from src.database import connection, initialize_db, Base
from src.main import get_application


@pytest.fixture
def api_config() -> ApiConfig:
    return TestApiConfig()


@pytest.fixture
def fastapi_app(api_config: ApiConfig) -> FastAPI:
    return get_application(config=api_config)


engine = create_engine("sqlite:///:memory:")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


async def test_connection():
    with SessionLocal() as session:
        yield session


@pytest.fixture
def client(fastapi_app: FastAPI) -> TestClient:
    fastapi_app.dependency_overrides[connection] = test_connection
    return TestClient(app=fastapi_app)
