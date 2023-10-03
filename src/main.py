from fastapi import FastAPI, Depends
from fastapi.security import HTTPBasic

from src.core.config import ApiConfig
from src.attend_workshop.router import router as attend_workshop_router
from src.database import connection
from src.signup.router import router as signup_router
from src.healthz.router import router as healthz_router
from starlette.middleware.cors import CORSMiddleware
from src.core.dependencies import get_api_config



def get_application(config: ApiConfig) -> FastAPI:
    app = FastAPI(
        title=config.project_name,
        version=config.version,
        debug=config.debug,
        dependencies=[Depends(connection)],
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )


    app.include_router(attend_workshop_router)
    app.include_router(signup_router)
    app.include_router(healthz_router)


    return app


app = get_application(config=get_api_config())
