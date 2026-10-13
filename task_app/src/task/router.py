from fastapi import APIRouter, Depends, status
from src.task import controller
from src.task.dtos import TaskSchema, TaskResponseSchema
from src.utils.db import get_db
from sqlalchemy.orm import Session
from src.user.models import UserModal
from src.task.models import TaskModal
from src.utils.helpers import isAuthroized


task_route = APIRouter(prefix="/task")

@task_route.post("/create", response_model = TaskResponseSchema)
def create_task(body:TaskSchema, db:Session = Depends(get_db), user:UserModal = Depends(isAuthroized)):
    return controller.createTask(body, db, user)


@task_route.get("/all_tasks", response_model = list[TaskResponseSchema])
def get_all_task(db:Session=Depends(get_db), user:UserModal = Depends(isAuthroized)):
    return controller.getTask(db, user)

@task_route.get("/get_task/{id}", response_model = TaskResponseSchema)
def get_task_withId(id:int, db:Session=Depends(get_db)):
    return controller.getTaskWithId(id, db)

@task_route.put('/update_task/{id}', response_model = TaskResponseSchema)
def update_task_withId(body: TaskSchema, id: int, db:Session=Depends(get_db)):
    print("I am in controller line 22")
    return controller.updateTask(body, id, db)


@task_route.delete('/delete_task/{id}')
def update_task_withId(id: int, db:Session=Depends(get_db)):
    return controller.deleteTask(id, db)


@task_route.delete("/delete")
def remove_all_task_with_null_Id(db:Session=Depends(get_db)):
    tasks = db.query(TaskModal).filter(
        TaskModal.user_id.is_(None)
    ).all()

    count = len(tasks)

    for task in tasks:
        db.delete(task)

    db.commit()

    return {
        "message": "Delete successful",
        "deleted_count": count
    }