from fastapi import FastAPI

from database import engine
from models import Base

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Question
from schemas import QuestionResponse
from typing import List

from fastapi import Depends

Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to QueryCraft!"}

@app.get("/questions", response_model=List[QuestionResponse])
def get_questions(db: Session = Depends(get_db)):
    questions = db.query(Question).all()
    return questions