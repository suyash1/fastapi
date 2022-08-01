import uvicorn
from fastapi import FastAPI

from utils.celery import create_celery
from routes import async_routes, list_cycle

def create_app() -> FastAPI:
    current_app = FastAPI(title="List Cycle and Asynchronous tasks processing with Celery and RabbitMQ",
                          description="Sample FastAPI Application to demonstrate Event "
                                      "driven architecture with Celery and RabbitMQ",
                          version="1.0.0", )

    current_app.celery_app = create_celery()
    current_app.include_router(list_cycle.router)
    current_app.include_router(async_routes.router)
    return current_app


app = create_app()
celery = app.celery_app
