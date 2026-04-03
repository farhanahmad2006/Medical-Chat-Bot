from fastapi import FastAPI, Request, Form, Depends, HTTPException, status, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import Optional
import shutil
import os
import uuid
import json

import models, schemas, auth, gemini_service
from database import engine, get_db

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Dependency to get current user from cookie
def get_current_user_from_cookie(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    if not token:
        return None
    try:
        scheme, _, param = token.partition(" ")
        # Support "Bearer <token>" or just "<token>"
        actual_token = param if scheme.lower() == 'bearer' else token
        return auth.get_current_user(actual_token, db)
    except Exception:
        return None

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, db: Session = Depends(get_db)):
    user = get_current_user_from_cookie(request, db)
    if user:
         return RedirectResponse(url="/home", status_code=status.HTTP_302_FOUND)
    return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)

@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
async def register(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    age: Optional[int] = Form(None),
    gender: Optional[str] = Form(None),
    location: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.email == email).first()
    if user:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Email already registered"})
    
    hashed_password = auth.get_password_hash(password)
    new_user = models.User(
        username=username,
        email=email,
        hashed_password=hashed_password,
        age=age,
        gender=gender,
        location=location
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user or not auth.verify_password(password, user.hashed_password):
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid username or password"})
    
    access_token = auth.create_access_token(data={"sub": user.username})
    response = RedirectResponse(url="/home", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    return response

@app.get("/logout")
async def logout():
    response = RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
    response.delete_cookie("access_token")
    return response

@app.get("/home", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(get_db)):
    user = get_current_user_from_cookie(request, db)
    if not user:
        return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)
    return templates.TemplateResponse("home.html", {"request": request, "user": user})

@app.post("/analyze")
async def analyze(
    request: Request,
    symptoms: str = Form(...),
    weight: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    user = get_current_user_from_cookie(request, db)
    if not user:
        return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)

    image_path = None
    if image and image.filename:
        upload_dir = "static/uploads"
        os.makedirs(upload_dir, exist_ok=True)
        filename = f"{uuid.uuid4()}_{image.filename}"
        image_path = os.path.join(upload_dir, filename)
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

    analysis_result = gemini_service.analyze_symptoms(
        symptoms=symptoms,
        weight=weight,
        age=user.age,
        gender=user.gender,
        image_path=image_path
    )

    history = models.MedicalHistory(
        user_id=user.id,
        symptoms=symptoms,
        weight=weight,
        report_image_path=image_path,
        gemini_response=analysis_result
    )
    db.add(history)
    db.commit()
    db.refresh(history)

    return templates.TemplateResponse("result.html", {
        "request": request,
        "user": user,
        "result": analysis_result,
        "symptoms": symptoms,
        "image_path": image_path
    })

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request, db: Session = Depends(get_db)):
    user = get_current_user_from_cookie(request, db)
    if not user:
        return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)
    
    history_records = db.query(models.MedicalHistory).filter(models.MedicalHistory.user_id == user.id).order_by(models.MedicalHistory.timestamp.desc()).all()
    
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "user": user,
        "history": history_records
    })

@app.get("/history/{history_id}", response_class=HTMLResponse)
async def get_history_item(request: Request, history_id: int, db: Session = Depends(get_db)):
    user = get_current_user_from_cookie(request, db)
    if not user:
        return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)
    
    record = db.query(models.MedicalHistory).filter(models.MedicalHistory.id == history_id, models.MedicalHistory.user_id == user.id).first()
    if not record:
        raise HTTPException(status_code=404, detail="History record not found")
        
    return templates.TemplateResponse("report_view.html", {
        "request": request,
        "user": user,
        "record": record,
        "json": json
    })

@app.post("/history/{history_id}/summarize")
async def summarize_history(request: Request, history_id: int, db: Session = Depends(get_db)):
    user = get_current_user_from_cookie(request, db)
    if not user:
        return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)
    
    record = db.query(models.MedicalHistory).filter(models.MedicalHistory.id == history_id, models.MedicalHistory.user_id == user.id).first()
    if not record:
        raise HTTPException(status_code=404, detail="History record not found")
        
    if not record.summary:
        summary = gemini_service.summarize_text(record.gemini_response)
        record.summary = summary
        db.commit()
        db.refresh(record)
    
    # Redirect back to the report view
    return RedirectResponse(url=f"/history/{history_id}", status_code=status.HTTP_303_SEE_OTHER)

@app.post("/history/{history_id}/find_doctors")
async def find_doctors(request: Request, history_id: int, db: Session = Depends(get_db)):
    user = get_current_user_from_cookie(request, db)
    if not user:
        return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)
    
    record = db.query(models.MedicalHistory).filter(models.MedicalHistory.id == history_id, models.MedicalHistory.user_id == user.id).first()
    if not record:
        raise HTTPException(status_code=404, detail="History record not found")
        
    if not record.doctors_recommendation:
        doctors_json = gemini_service.get_doctors_list(record.symptoms, user.location)
        record.doctors_recommendation = doctors_json
        db.commit()
        db.refresh(record)
    
    # Redirect back to the report view
    return RedirectResponse(url=f"/history/{history_id}", status_code=status.HTTP_303_SEE_OTHER)
