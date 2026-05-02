from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import jwt

import models, schemas, crud
from database import engine
from crud import get_current_user
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/signup", response_model=schemas.User)
def signup(user: schemas.UserCreate, db: Session = Depends(crud.get_db)):
    if crud.get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email exists")
    return crud.create_user(db, user)

@app.post("/token")
def login(form_data=Depends(crud.oauth2_scheme), db: Session = Depends(crud.get_db)):
    # NOTE: simplified, better keep original form handler if needed
    pass