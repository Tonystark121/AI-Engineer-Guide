from fastapi import APIRouter
from src import controller
from src.modal import TaskSchema

router = APIRouter(prefix= "/tasks")

@router.get('/')
def getTask():
    return controller.getTaskMethod()

@router.get('/{task_id}')
def getTaskwithId(task_id:int):
    print(id)
    return  controller.getTaskwithIdMethod(task_id)


@router.post('/')
def createTask(body:TaskSchema):
    print("Post method called")
    return controller.createTaskMethod(body)


@router.post('/{task_id}')
def updateTask(body:TaskSchema, task_id:int):
    return controller.updateTaskMethod(body, task_id)


@router.delete('/{task_id}')
def deleteTask(task_id:int):
    return controller.deleteTaskMethod(task_id)

