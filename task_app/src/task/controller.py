from src.task.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.task.models import TaskModal

# create task method
def createTask(body:TaskSchema, db: Session):
    print(body.model_dump())
    data = body.model_dump()
    new_Task = TaskModal(title=data['title'], desc = data['desc'], is_complete = data['is_complete'])
    
    db.add(new_Task)
    db.commit()
    db.refresh(new_Task)
    return {"message": "Task created Successfully....", "data": new_Task}


def getTask(db: Session):
    tasks =  db.query(TaskModal).all()
    return {
        "Status": 200,
        "message": "Fetched Tasks Successful",
        "tasks": tasks
    }