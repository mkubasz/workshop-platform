from fastapi import FastAPI
from src.api.config import ApiConfig
from src.endpoints import attend_workshop, signup, healthz
from starlette.middleware.cors import CORSMiddleware
from src.api.dependencies import get_api_config


def get_application(config: ApiConfig) -> FastAPI:
    app = FastAPI(
        title=config.project_name,
        version=config.version,
        debug=config.debug,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )


    app.include_router(signup.router)
    app.include_router(attend_workshop.router)
    app.include_router(healthz.router)


    return app

app = get_application(config=get_api_config())
