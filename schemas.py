from pydantic import BaseModel
from typing import Optional


class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int


class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int


class CreateTask(BaseModel):
    title: str
    content: str
    priority: Optional[int] = 0


class UpdateTask(BaseModel):
    title: str
    content: str
    priority: Optional[int] = 0

