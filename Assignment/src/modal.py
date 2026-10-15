
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class TaskSchema(BaseModel):
    title: str = Field(min_length=1, max_length=1000)
    description: str
    is_complete: bool = False
    createdDate: datetime = Field(default_factory=datetime.now)


class TaskResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str
    is_complete: bool
    createdDate: datetime

