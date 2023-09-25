from datetime import datetime

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from src.core.dependencies import get_api_config

from sqlalchemy import create_engine, String, DateTime, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column

from src.database import Base, connection

router = APIRouter()



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



class Signup(BaseModel):
    discord_id: str
    name: str
    password: str
    email: str
    invoice: str


@router.post("/signup", status_code=201)
async def signup(signup: Signup, session_connection: sessionmaker = Depends(connection)):
    attendees = Attendees(
        name=signup.name,
        password=signup.password,
              email=signup.email,
              invoice=signup.invoice,)
    session = session_connection()
    session.add(attendees)
    session.commit()
    return {"status": "ok"}
