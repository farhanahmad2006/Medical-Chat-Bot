# MediBot - Medical Chatbot Application

A responsive, AI-powered medical chatbot that analyzes symptoms, tracks medical history, and recommends nearby doctors.

## Prerequisites

Before running the project, ensure you have the following installed:

1.  **Python 3.9+**: [Download Here](https://www.python.org/downloads/)
2.  **MySQL Server (or XAMPP/MariaDB)**: [Download XAMPP](https://www.apachefriends.org/download.html)
3.  **Google Gemini API Key**: [Get Key Here](https://aistudio.google.com/app/apikey)

## Installation Guide

Follow these steps to set up the project locally.

### 1. Clone/Download the Project
Navigate to the project directory:
```bash
cd medical_chatbot
```

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.
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
1.  Start your MySQL Server (e.g., open XAMPP and start specific "MySQL").
2.  Create a new database named `medical_chatbot_db` in your MySQL client (like phpMyAdmin or Workbench).
    ```sql
    CREATE DATABASE medical_chatbot_db;
    ```
3.  The application will automatically create the necessary tables (`users`, `medical_history`) when run for the first time.

### 5. Environment Configuration
Create a `.env` file in the root directory and add the following configurations:

```ini
# Database Connection String
# Format: mysql+mysqlconnector://<USER>:<PASSWORD>@<HOST>/<DATABASE_NAME>
DATABASE_URL=mysql+mysqlconnector://root:@localhost/medical_chatbot_db

# Google Gemini API Key
GEMINI_API_KEY=your_actual_api_key_here

# Secret Key for Security (Generate a random string)
SECRET_KEY=supersecretkey123
```

### 6. Run the Application
Start the local server using Uvicorn:

```bash
uvicorn main:app --reload
```
*   `--reload`: Enables auto-restart when code changes.

## Usage

1.  Open your browser and go to: `http://127.0.0.1:8000`
2.  **Register** a new account.
3.  **Login** with your credentials.
4.  **Home Page**: Enter your symptoms (e.g., "fever and rash") and upload an image if needed.
5.  **Result**: View the AI analysis.
6.  **Dashboard**: See your history, click "View Report" for details.
7.  **Find Doctor**: Use the "Find Doctor" button in the report to search for specialists on Google Maps.

## Troubleshooting

*   **Error: Module not found**: Ensure you activated the virtual environment and ran `pip install -r requirements.txt`.
*   **Database Error**: Check if your MySQL server is running and the credentials in `.env` are correct.
*   **Gemini Error**: Ensure your API key is valid and you have internet access.
