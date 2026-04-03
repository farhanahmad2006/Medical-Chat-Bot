from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
    age = Column(Integer, nullable=True)
    gender = Column(String(10), nullable=True)
    location = Column(String(100), nullable=True)

    history = relationship("MedicalHistory", back_populates="user")

class MedicalHistory(Base):
    __tablename__ = "medical_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    symptoms = Column(Text)
    weight = Column(String(20), nullable=True) # Storing as string to allow units if needed or simple float
    report_image_path = Column(String(255), nullable=True)
    gemini_response = Column(Text) # Storing the full analysis
    summary = Column(Text, nullable=True) # Short summary of the report
    doctors_recommendation = Column(Text, nullable=True) # JSON string of recommended doctors
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="history")
