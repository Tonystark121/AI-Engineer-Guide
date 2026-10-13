from pydantic import BaseModel, ConfigDict

class TaskSchema(BaseModel):
    title : str
    desc : str
    is_complete : bool = False
    
class TaskResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : int
    title : str
    desc: str
    user_id: int