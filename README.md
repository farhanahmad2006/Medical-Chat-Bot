# 🏥 MediBot - Medical Chatbot Application

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)
![Gemini AI](https://img.shields.io/badge/AI-Google_Gemini-blueviolet.svg)

A responsive, AI-powered medical chatbot designed to analyze patient symptoms, track medical history, summarize reports, and recommend nearby doctors based on geolocation and symptoms.

## ✨ Features

- 🩺 **Symptom Analysis:** Powered by Google's Gemini Pro AI to evaluate text and image-based symptoms.
- 🔐 **Secure User Authentication:** JWT-based login and registration system.
- 📊 **Patient Dashboard:** Keep track of all generated reports and past analyses securely.
- 📝 **AI Report Summarization:** Automatically summarizes long AI-generated analysis.
- 🏥 **Find a Doctor:** Built-in integration to search for specialized doctors nearby on Google Maps.
- 📱 **Responsive UI:** Clean, mobile-friendly interface built with HTML, CSS, and Bootstrap.

---

## 🛠 Prerequisites

Before running the project, ensure you have the following installed:

1. **Python 3.9+**: [Download Here](https://www.python.org/downloads/)
2. **MySQL Server (or XAMPP/MariaDB)**: [Download XAMPP](https://www.apachefriends.org/download.html)
3. **Google Gemini API Key**: [Get Key Here](https://aistudio.google.com/app/apikey)

---

## 🚀 Installation Guide

Follow these steps to set up the project locally.

### 1. Clone/Download the Project
Navigate to your desired folder and clone the repository:
```bash
git clone https://github.com/farhanahmad2006/Medical-Chat-Bot.git
cd Medical-Chat-Bot
```

### 2. Create a Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies securely.
```bash
python -m venv venv

# Activate on Windows:
.\venv\Scripts\activate

# Activate on Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
Install all required Python packages using pip:
```bash
pip install -r requirements.txt
```

### 4. Database Setup
1. Start your MySQL Server (e.g., via XAMPP).
2. Create a new database named `medical_chatbot_db` in your MySQL client (like phpMyAdmin or Workbench).
   ```sql
   CREATE DATABASE medical_chatbot_db;
   ```
3. The application will automatically create the necessary tables (`users`, `medical_history`) when it runs for the first time.

### 5. Environment Configuration
Create a `.env` file in the root directory (you can copy the `.env.sample` file to get started).
Ensure it has the following configurations:

```ini
# Database Connection String
# Format: mysql+mysqlconnector://<USER>:<PASSWORD>@<HOST>:<PORT>/<DATABASE_NAME>
DATABASE_URL=mysql+mysqlconnector://root:YOUR_PASSWORD@localhost:3306/medical_chatbot_db

# Google Gemini API Key
GEMINI_API_KEY=your_actual_api_key_here

# Secret Key for Security (Generate a random string)
SECRET_KEY=supersecretkey123
```

---

## 💻 Running the Application

Start the local server using Uvicorn:

```bash
uvicorn main:app --reload
```
*`--reload` enables auto-restart when code changes are detected.*

---

## 📖 Usage Instructions

1. Open your browser and navigate to: `http://127.0.0.1:8000`
2. **Register** a new account and log in.
3. **Home Page**: Enter your symptoms (e.g., "fever and rash") and upload a visual image if needed.
4. **Result**: View the comprehensive AI analysis.
5. **Dashboard**: See your entire medical history. Click "View Report" for details.
6. **Find Doctor**: Use the "Find Doctor" button inside the report to search for relevant specialists nearby on Google Maps.

---

## ⚠️ Troubleshooting

- **Error: Module not found**: Ensure your virtual environment is activated and you ran `pip install -r requirements.txt`.
- **Database Error**: Check if your MySQL server is running, the port is correct, and the credentials in `.env` match.
- **Gemini Error**: Ensure your API key is correctly copied without extra spaces and you have active internet access.
- **Git Push Error (.env)**: We provided a `.env.sample` and added `.env` to `.gitignore` to protect your sensitive API keys. Make sure your real keys only live in your local `.env` file.

---
*Created for the Medical Chatbot Project.*
