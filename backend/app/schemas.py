from pydantic import BaseModel, ConfigDict
from datetime import datetime
from enum import Enum

class TaskStatus(str, Enum):
    open = "open"
    in_progress = "doing"
    complete = "complete"

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    status: TaskStatus 
    due_date: datetime

class TaskResponse(TaskCreate):
    id:int
    created_at: datetime

    #required since i'm returning an ORM model (gets rid of a Type Error)
    model_config = ConfigDict(from_attributes=True)
