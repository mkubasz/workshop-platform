from typing import Annotated

from fastapi import APIRouter, Body, HTTPException, Depends

from src.attend_workshop.model import AttendWorkshopData
from src.attend_workshop.service import assign_attendee
from src.auth.validate import validate_credentials
from src.core.results import Result

router = APIRouter()

class WorkshopProvider:
    def getById(self, workshop_id):
        pass

class AttendeeWorkshopProvider:
    def findByWorkshop(self):
        pass

@router.post(
    "/workshop/attend",
    status_code=201,
    dependencies=[Depends(validate_credentials)])
async def attend_workshop(attend_workshop_command: Annotated[AttendWorkshopData, Body()] = ...,):
    ticket_result: Result = assign_attendee(attend_workshop_command, WorkshopProvider(), AttendeeWorkshopProvider())
    if not ticket_result.is_ok():
        raise HTTPException(status_code=404, detail=ticket_result.error)

    return {
        "status": "ok",
        "ticket": ticket_result.data,
    }
