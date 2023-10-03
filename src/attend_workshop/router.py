from typing import Annotated

from fastapi import APIRouter, Body, HTTPException, Depends

from src.attend_workshop.model import AttendWorkshop
from src.attend_workshop.service import assign_attendee
from src.auth.validate import validate_credentials
from src.core.results import Result

router = APIRouter()


@router.post("/workshop/attend", status_code=201, dependencies=[Depends(validate_credentials)])
async def attend_workshop(attend_workshop_query: Annotated[AttendWorkshop, Body()] = ...,):
    ticket_result: Result = assign_attendee(attend_workshop_query)
    if ticket_result.is_ok():
        return {
            "status": "ok",
            "ticket": ticket_result.data
        }
    else:
        raise HTTPException(status_code=404, detail=ticket_result.error)

