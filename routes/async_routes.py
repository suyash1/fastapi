from celery import group
from fastapi import APIRouter
from starlette.responses import JSONResponse

from celery_tasks.tasks import get_something_done_task
from utils.celery import get_task_info

router = APIRouter(tags=['Async routes'], responses={404: {"description": "Not found"}})


@router.post("/async")
async def get_something_done():
    """
    Return the List of universities for the countries for e.g ["turkey","india","australia"] provided
    in input in a async way. It just returns the task id, which can later be used to get the result.
    """
    task = get_something_done_task.apply_async()
    return JSONResponse({"task_id": task.id})


@router.get("/task/{task_id}")
async def get_task_status(task_id: str) -> dict:
    """
    Return the status of the submitted Task
    """
    return get_task_info(task_id)


