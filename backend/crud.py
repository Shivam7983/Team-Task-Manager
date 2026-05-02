from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt, JWTError
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime

import models
from database import SessionLocal
from config import SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------- AUTH ----------------
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user):
    hashed = pwd_context.hash(user.password)
    db_user = models.User(name=user.name, email=user.email, password_hash=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not pwd_context.verify(password, user.password_hash):
        return None
    return user

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

# ---------------- PROJECT ----------------
def create_project(db: Session, project, admin_id: int):
    db_project = models.Project(name=project.name, description=project.description, admin_id=admin_id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def add_project_member(db: Session, project_id: int, user_id: int):
    existing = db.query(models.ProjectMember).filter_by(project_id=project_id, user_id=user_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Already member")

    db_member = models.ProjectMember(project_id=project_id, user_id=user_id)
    db.add(db_member)
    db.commit()
    return db_member

def check_admin(db: Session, project_id: int, user_id: int):
    project = db.query(models.Project).filter_by(id=project_id).first()
    if not project or project.admin_id != user_id:
        raise HTTPException(status_code=403, detail="Not admin")

def check_project_access(db: Session, project_id: int, user_id: int):
    member = db.query(models.ProjectMember).filter_by(project_id=project_id, user_id=user_id).first()
    if not member:
        raise HTTPException(status_code=403, detail="No access")

# ---------------- TASK ----------------
def create_task(db: Session, task):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter_by(id=task_id).first()

def update_task_status(db: Session, task_id: int, status: str):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.status = status
    db.commit()
    return task

# ---------------- DASHBOARD ----------------
def get_total_tasks(db: Session, user_id: int):
    return db.query(models.Task).filter_by(assigned_to=user_id).count()

def get_overdue_tasks(db: Session, user_id: int):
    return db.query(models.Task).filter(
        models.Task.assigned_to == user_id,
        models.Task.due_date < datetime.utcnow()
    ).count()