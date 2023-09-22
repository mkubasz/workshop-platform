import os
from datetime import datetime

import httpx
from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from src.core.dependencies import get_api_config

config = get_api_config()

router = APIRouter()


class Signup(BaseModel):
    discord_id: str
    name: str
    password: str
    email: str
    invoice: str
    created_at: datetime = datetime.now()


@router.post("/signup", status_code=201)
async def signup(signup: Signup):
    request_body = {
        "parent": {
            "database_id": config.DATABASE_ID
        },
        "properties": {
            "discord_id": {
                "title": [
                    {
                        "text": {
                            "content": signup.discord_id
                        }
                    }
                ]
            },
            "name": {
                "rich_text": [
                    {
                        "text": {
                            "content": signup.name
                        }
                    }]
            },
            "password": {
                "rich_text": [
                    {
                        "text": {
                            "content": signup.password
                        }
                    }
                ]
            },
            "email": {
                "email": signup.email
            },
            "invoice": {
                "rich_text": [
                    {
                        "text": {
                            "content": signup.invoice
                        }
                    }
                ]
            }
        }
    }

    status = httpx.post(
        "https://api.notion.com/v1/pages",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {config.AUTHORIZATION}",
            "Notion-Version": "2022-06-28",
        },
        json=request_body
    )
    if status.status_code == 201:
        return {"status": "ok"}

    return JSONResponse(status_code=400, content={"status": "error"})
