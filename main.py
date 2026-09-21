from fastapi import FastAPI

from database import engine
from models import Base

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Question
from schemas import QuestionResponse, QuestionCreate
from typing import List

from fastapi import Depends

from passlib.context import CryptContext

from models import Submission
from schemas import SubmissionCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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

@app.post("/questions", response_model=QuestionResponse)
def create_question(question: QuestionCreate, db: Session = Depends(get_db)):
    new_question = Question(**question.dict())
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question

from models import User
from schemas import UserCreate

@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(user.password)
    new_user = User(name=user.name, email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully", "user_id": new_user.id}

@app.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not pwd_context.verify(password, user.password):
        return {"error": "Invalid email or password"}
    return {"message": "Login successful", "user_id": user.id}

@app.post("/submissions")
def create_submission(submission: SubmissionCreate, db: Session = Depends(get_db)):
    new_submission = Submission(
        user_id=submission.user_id,
        question_id=submission.question_id,
        submitted_query=submission.submitted_query,
        is_correct=0
    )
    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)
    return {"message": "Submission recorded", "submission_id": new_submission.id}