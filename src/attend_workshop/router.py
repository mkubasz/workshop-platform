from typing import Annotated

from fastapi import APIRouter, Body
from pydantic import BaseModel

from src.attend_workshop.domain import check_if_attendee_is_signed_up, Workshop, AttendeeWorkshop, \
    check_if_workshop_is_open, check_if_attendee_has_already_attended, check_if_workshop_has_exceeded_limits, \
    assign_attendee_to_workshop

router = APIRouter()


class AttendWorkshop(BaseModel):
    discord_id: str
    workshop_id: str


def event_handler(event):
    pass


@router.post("/workshop/attend", status_code=201)
async def attend_workshop(attend_workshop: Annotated[AttendWorkshop, Body()] = ...,):
    check_if_attendee_is_signed_up(attend_workshop.discord_id)
    workshop = Workshop(attend_workshop.workshop_id)
    attendee_workshop = AttendeeWorkshop()
    check_if_workshop_is_open(workshop)
    check_if_attendee_has_already_attended(attend_workshop.discord_id)
    check_if_workshop_has_exceeded_limits(workshop, attendee_workshop)
    event = assign_attendee_to_workshop(attend_workshop.workshop_id, attend_workshop.discord_id)
    ticket = event_handler(event)
    return {
        "status": "ok",
        "ticket": ticket
    }
