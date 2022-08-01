import asyncio
from fastapi import APIRouter, UploadFile, File
from starlette.responses import JSONResponse

import asyncio
from utils import helpers
import json

router = APIRouter()

@router.get("/health")
async def root():
    return {"message": "I'm alive!!!"}


@router.post("/upload-list-file/")
async def create_upload_file(uploaded_file: UploadFile = File(...)):
    json_data = json.load(uploaded_file.file)
    return JSONResponse({
        list_name : await asyncio.create_task(helpers.check_cycle_in_list(list_data)) for list_name, list_data in json_data.items()
        })

