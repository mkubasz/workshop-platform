from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/attend/workshop", status_code=201)
async def attend_workshop(discord_id: str, workshop_id: str):
    return JSONResponse(status_code=400, content={"status": "ERROR"})