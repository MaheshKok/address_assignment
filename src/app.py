from fastapi import FastAPI

from src.routers.initializer import IncludeAPIRouter


def create_web_app() -> FastAPI:
    """
    Registers Json Routes

    Returns: FastAPI app
    """
    app = FastAPI()
    app.include_router(IncludeAPIRouter())

    return app
