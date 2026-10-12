from fastapi import APIRouter, Depends
from src.task import controller
from src.task.dtos import TaskSchema
from src.utils.db import get_db
task_route = APIRouter(prefix="/task")

@task_route.post("/create")
def create_task(body:TaskSchema, db = Depends(get_db)):
    return controller.createTask(body, db)


@task_route.get("/all_tasks")
def get_all_task(db=Depends(get_db)):
    return controller.getTask(db)

@task_route.get("/get_task/{id}")
def get_task_withId(id:int, db=Depends(get_db)):
    return controller.getTaskWithId(id, db)

@task_route.put('/update_task/{id}')
def update_task_withId(body: TaskSchema, id: int, db=Depends(get_db)):
    print("I am in controller line 22")
    return controller.updateTask(body, id, db)


@task_route.delete('/delete_task/{id}')
def update_task_withId(id: int, db=Depends(get_db)):
    return controller.deleteTask(id, db)