from src.task.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.task.models import TaskModal
from fastapi import HTTPException

# create task method
def createTask(body:TaskSchema, db: Session):
    print(body.model_dump())
    data = body.model_dump()
    new_Task = TaskModal(title=data['title'], desc = data['desc'], is_complete = data['is_complete'])
    
    db.add(new_Task)
    db.commit()
    db.refresh(new_Task)
    return new_Task


def getTask(db: Session):
    tasks =  db.query(TaskModal).all()
    print(tasks)
    return tasks
    
def getTaskWithId(id: int, db:Session):
    task = db.query(TaskModal).get(id)
    if not task:
        return HTTPException(404, "No related task found, please enter a valid id")
    
    return task
    
def updateTask(body: TaskSchema, id: int, db:Session):
    task = db.query(TaskModal).filter(TaskModal.id == id).first()
    print(body)
    if not task:
        return HTTPException(404, "No related task found, please enter a valid id")
    
    body = body.model_dump(exclude_unset=True)
    print("I am in controller line 44")
    for field, value in body.items():
        setattr(task, field, value)
        
    db.commit()
    db.refresh(task)
    
    return task


def deleteTask(id: int, db=Session):
    task = db.query(TaskModal).filter(TaskModal.id == id).first()
    if not task:
        return HTTPException(404, "No related task found, please enter a valid id")
    
    db.delete(task)
    db.commit()
    return None