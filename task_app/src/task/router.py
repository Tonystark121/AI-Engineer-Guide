from fastapi import APIRouter, Depends
from src.task import controller
from src.task.dtos import TaskSchema
from src.utils.db import get_db
task_route = APIRouter(prefix="/task")

@task_route.post("/create")
def create_task(body:TaskSchema, db = Depends(get_db)):
    return controller.createTask(body, db)


@task_route.get("/get")
def get_all_task(db=Depends(get_db)):
    return controller.getTask(db)