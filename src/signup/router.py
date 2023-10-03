from datetime import datetime
from typing import Annotated
from fastapi import APIRouter, Depends, Body
from pydantic import BaseModel, Field, EmailStr

from sqlalchemy import String, DateTime, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column

from src.auth.password_util import hash_password
from src.database import Base, connection

router = APIRouter()


class Signup(BaseModel):
    discord_id: str = Field(
        description="This is name of user find in Discord",
        examples=["mkubasz"]
    )
    name: str = Field(description="You can use any name")
    password: str = Field(description="This value will be hashed", min_length=8)
    email: EmailStr
    invoice: str = Field(
        description="Information should contain VAT number, Company name, address"
    )


class Attendees(Base):
    __tablename__ = "attendees"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    password: Mapped[LargeBinary] = mapped_column(LargeBinary(256))
    email: Mapped[str] = mapped_column(String(50))
    invoice: Mapped[str] = mapped_column(String(512))
    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


@router.post("/signup", status_code=201)
async def signup(signup: Annotated[Signup, Body()],
                 session: Annotated[Base, Depends(connection)]):
    attendees = Attendees(
        name=signup.name,
        password=hash_password(signup.password),
        email=signup.email,
        invoice=signup.invoice,
    )
    session.add(attendees)
    session.commit()
    return {"status": "ok"}
