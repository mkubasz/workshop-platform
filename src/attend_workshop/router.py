from typing import Annotated

from fastapi import APIRouter, Body
from pydantic import BaseModel

router = APIRouter()


class AttendWorkshop(BaseModel):
    discord_id: str
    workshop_id: str


@router.post("/workshop/attend", status_code=201)
async def attend_workshop(attend_workshop: Annotated[AttendWorkshop, Body()] = ...,):
    # Check if attendee exists
    # Check if workshop exists
    # Check if workshop is open
    # Check if workshop is full
    # Check if attendee has already attended
    # Check if reserved list to workshop is full
    # Add attendee to workshop
    return {"status": "ok"}
