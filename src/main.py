from fastapi import FastAPI
from dotenv import load_dotenv

from src import attend_workshop, signup

load_dotenv()

app = FastAPI()


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}


app.include_router(signup.router)
app.include_router(attend_workshop.router)
