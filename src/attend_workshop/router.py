from typing import Annotated

from fastapi import APIRouter, Body, HTTPException
from pydantic import BaseModel

from src.attend_workshop.service import assign_attendee
from src.core.results import Result

router = APIRouter()


class AttendWorkshop(BaseModel):
    discord_id: str
    workshop_id: str


@router.post("/workshop/attend", status_code=201)
async def attend_workshop(attend_workshop_query: Annotated[AttendWorkshop, Body()] = ...,):
    ticket_result: Result = assign_attendee(attend_workshop_query)
    if ticket_result.is_ok():
        return {
            "status": "ok",
            "ticket": ticket_result.data
        }
    else:
        raise HTTPException(status_code=404, detail=ticket_result.error)

