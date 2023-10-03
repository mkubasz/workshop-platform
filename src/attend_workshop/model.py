from pydantic import BaseModel


class AttendWorkshop(BaseModel):
    discord_id: str
    workshop_id: str
