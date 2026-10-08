from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

    

class TaskCreate(BaseModel):
    title: str
    

class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool
    owner_id: int

    model_config = {"from_attributes": True}