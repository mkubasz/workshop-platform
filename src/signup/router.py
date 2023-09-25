from datetime import datetime

import httpx
from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from src.core.dependencies import get_api_config

config = get_api_config()

router = APIRouter()
from sqlalchemy import create_engine, String, DateTime, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column

url_postgresql = URL.create(
    drivername="postgresql",
    username=config.DATABASE_USERNAME,
    password=config.DATABASE_PASSWORD,
    host=config.DATABASE_HOST,
    port=5432,
    database=config.DATABASE_NAME
)
engine = create_engine(
     url_postgresql
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
session = SessionLocal()


class Attendees(Base):
    __tablename__ = "attendees"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(256))
    email: Mapped[str] = mapped_column(String(50))
    invoice: Mapped[str] = mapped_column(String(512))
    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


Base.metadata.create_all(engine)

class Signup(BaseModel):
    discord_id: str
    name: str
    password: str
    email: str
    invoice: str


@router.post("/signup", status_code=201)
async def signup(signup: Signup):
    attendees = Attendees(
        name=signup.name,
        password=signup.password,
              email=signup.email,
              invoice=signup.invoice,)
    session.add(attendees)
    session.commit()
    return {"status": "ok"}
