from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    
class QuestionResponse(BaseModel):
    id: int
    title: str
    description: str
    difficulty: str
    topic: str

    class Config:
        from_attributes = True
        
        
class QuestionCreate(BaseModel):
    title: str
    description: str
    difficulty: str
    topic: str