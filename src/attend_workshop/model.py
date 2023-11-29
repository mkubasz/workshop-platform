from pydantic import BaseModel
from src.core.command import Command
from src.core.event import Event


class AttendWorkshopData(BaseModel):
    discord_id: str
    workshop_id: str


class AttendWorkshopCommand(Command[AttendWorkshopData]):
    type = 'AttendWorkshop'
    data: AttendWorkshopData


class AttendedWorkshop(Event[AttendWorkshopData]):
    type = 'AttendedWorkshop'
    data: AttendWorkshopData
