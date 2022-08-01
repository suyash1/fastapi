import uvicorn as uvicorn
from fastapi import FastAPI, File, UploadFile
from starlette.responses import JSONResponse

import json
import asyncio
import time

from utils.celery import create_celery
from routes import async_routes, list_cycle



# from utils import helpers

# app = FastAPI()


# @app.get("/health")
# async def root():
#     return {"message": "I'm alive!!!"}


# @app.post("/upload-list-file/")
# async def create_upload_file(uploaded_file: UploadFile = File(...)):
#     json_data = json.load(uploaded_file.file)
#     return JSONResponse({
#         list_name : await asyncio.create_task(helpers.check_cycle_in_list(list_data)) for list_name, list_data in json_data.items()
#         })


def create_app() -> FastAPI:
    current_app = FastAPI(title="Asynchronous tasks processing with Celery and RabbitMQ",
                          description="Sample FastAPI Application to demonstrate Event "
                                      "driven architecture with Celery and RabbitMQ",
                          version="1.0.0", )

    current_app.celery_app = create_celery()
    current_app.include_router(list_cycle.router)
    current_app.include_router(async_routes.router)
    return current_app


app = create_app()
celery = app.celery_app