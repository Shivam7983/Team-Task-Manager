from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class User(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True

class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None

class Project(BaseModel):
    id: int
    name: str
    description: Optional[str]

    class Config:
        from_attributes = True

class MemberAdd(BaseModel):
    user_id: int

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: datetime
    priority: str
    status: str
    project_id: int
    assigned_to: int

class Task(BaseModel):
    id: int
    title: str
    status: str

    class Config:
        from_attributes = True

class TaskStatus(BaseModel):
    status: str