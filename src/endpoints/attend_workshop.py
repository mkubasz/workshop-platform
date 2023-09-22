from fastapi import APIRouter

router = APIRouter()


@router.post("/workshop/attend", status_code=201)
async def attend_workshop(discord_id: str, workshop_id: str):
    return {"status": "ok"}
