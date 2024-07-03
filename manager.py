from fastapi import FastAPI

from core.router import router as user_router
from core.handlers.file import router as file_router

def create_app() -> FastAPI:
    app = FastAPI(
        title='FastAPI ChatGPT pdf/excel formater',
        docs_url='/api/docs',
    )
    app.include_router(
        user_router,
        prefix='/api/v1',
    )
    app.include_router(
        file_router,
        prefix='/api/v1'
    )
    return app