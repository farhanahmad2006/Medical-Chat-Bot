from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str
    age: Optional[int] = None
    gender: Optional[str] = None
    location: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(UserBase):
    id: int
    class Config:
        orm_mode = True

class SymbolAnalysisRequest(BaseModel):
    symptoms: str
    weight: Optional[str] = None
    # Image will be handled via UploadFile in FastAPI, not Pydantic schema for the request body usually

class MedicalHistoryResponse(BaseModel):
    id: int
    symptoms: str
    weight: Optional[str] = None
    gemini_response: str
    timestamp: datetime
    report_image_path: Optional[str] = None

    class Config:
        orm_mode = True
