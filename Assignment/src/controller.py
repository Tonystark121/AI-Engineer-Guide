
from src import taskDetails
from src.modal import TaskSchema
from datetime import datetime
# define business logic here

def createTaskMethod(body: TaskSchema):
    if not body:
        return {
            "error": "Please enter task details to be created",
            "StatusCode": 400
        }

    if not body.title or not body.title.strip():
        return {
            "error": "Task title can't be empty",
            "StatusCode": 400
        }

    taskDetails.counter += 1

    details = body.model_dump()
    details["id"] = taskDetails.counter
    details["createdDate"] = datetime.now()

    taskDetails.taskList.append(details)

    return {
        "message": "Task Created Successfully",
        "tasks": details,
        "StatusCode": 201
    }



def getTaskMethod():
    return {"message": "Task Fetched Successfully", "StatusCode": 200, "tasks": taskDetails.taskList}

def getTaskwithIdMethod(task_id: int):
    if task_id > len(taskDetails.taskList):
        return {
            "message": "No related task found, please enter correct id",
            "StatusCode": 404
        }

    for task in taskDetails.taskList:
        if(task.id == task_id):
            return {
                "message": "Task Fetch Successful",
                "task": task,
                "StatusCode": 200
            }

    return {
            "message": "No related task found, please enter correct id",
                "StatusCode": 404
        }




def updateTaskMethod(body: TaskSchema, id: int):
    if id > len(taskDetails.taskList):
            return {
                "message": "No related task found, please enter correct id",
                "StatusCode": 404
            }
    details = body.model_dump(exclude_unset=True)
    for task in taskDetails.taskList:
            if(task.id == id):
                 task.title = details.title
                 task.description = details.description
                 task.is_complete = details.is_complete

                 return {
                         "message": "Task Update Successful",
                         "task": task,
                         "StatusCode": 200
                        }
                
    return {
            "message": "No related task found, please enter correct id",
                "StatusCode": 404
        }


def deleteTaskMethod(id: int):
    for index, task in enumerate(taskDetails.taskList):
        if task["id"] == id:
            deleted_task = taskDetails.taskList.pop(index)

            return {
                "message": "Task Deleted Successfully",
                "task": deleted_task,
                "StatusCode": 200
            }

    return {
        "message": "No related task found, please enter correct id",
        "StatusCode": 404
    }
