import os
from datetime import datetime

import httpx
from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse

DATABASE_ID = os.getenv('ATTENDEE_DATABASE_ID')
AUTHORIZATION = os.getenv('AUTHORIZATION')

router = APIRouter()
class Attendee(BaseModel):
    discord_id: str
    name: str
    password: str
    email: str
    invoice: str
    created_at: datetime = datetime.now()


@router.post("/signup/", status_code=201)
async def signup(attendee: Attendee):
    request_body = {
        "parent": {
            "database_id": DATABASE_ID
        },
        "properties": {
            "discord_id": {
                "title": [
                    {
                        "text": {
                            "content": attendee.discord_id
                        }
                    }
                ]
            },
            "name": {
                "rich_text": [
                    {
                        "text": {
                            "content": attendee.name
                        }
                    }]
            },
            "password": {
                "rich_text": [
                    {
                        "text": {
                            "content": attendee.password
                        }
                    }
                ]
            },
            "email": {
                "email": attendee.email
            },
            "invoice": {
                "rich_text": [
                    {
                        "text": {
                            "content": attendee.invoice
                        }
                    }
                ]
            }
        }
    }
    status = httpx.post(
        f"https://api.notion.com/v1/pages",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {AUTHORIZATION}",
            "Notion-Version": "2022-06-28",
        },
        json=request_body
    )
    if status.status_code == 201:
        return {"status": "OK"}

    return JSONResponse(status_code=400, content={"status": "ERROR"})