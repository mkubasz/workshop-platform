from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
import attend_workshop
import signup

app = FastAPI()

@app.get("/healthz/")
async def healthz():
    return {"status": "OK"}

app.include_router(signup.router)
app.include_router(attend_workshop.router)