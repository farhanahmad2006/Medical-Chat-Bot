# MediBot - AI Powered Medical Assistant
## Project Documentation

---

### 1. Project Description (Abstract)

MediBot is an advanced AI-powered medical chatbot application designed to accessible, preliminary healthcare guidance. Built using **FastAPI** for high-performance backend processing and **MySQL** for robust data management, the system integrates Google's **Gemini AI** to analyze reported symptoms and patient images. Users can register securely, submit their symptoms along with optional images (e.g., skin conditions), and receive an instant, intelligent assessment of potential conditions and severity.

Beyond simple analysis, MediBot features a comprehensive patient dashboard that tracks medical history over time. Key features include a "Find Doctor" smart search that locates nearby specialists based on the specific diagnosis, and an automated report summarization tool for quick review. The application features a responsive, premium "Glassmorphism" UI built with Bootstrap 5, ensuring a seamless experience across devices. MediBot aims to bridge the gap between initial symptom onset and professional medical consultation.

---

### 2. Project Presentation (10 Slides)

**Slide 1: Title Slide**
*   **Title:** MediBot: AI-Driven Healthcare Assistant
*   **Subtitle:** Bridging the Gap Between Symptoms and Specialists
*   **Team/Name:** Farhan
*   **Visual:** MediBot Logo / Screenshots of Home Page

**Slide 2: The Problem**
*   **Challenge:** Limited access to immediate medical advice.
*   **Pain Point:** Anxiety caused by unknown symptoms.
*   **Gap:** Difficulty finding the *right* specialist for a specific condition.

**Slide 3: The Solution**
*   **Core Idea:** An intelligent chatbot that analyzes symptoms and guides patients.
*   **Key Features:**
    *   AI Symptom Analysis (Text & Image).
    *   Secure Patient Dashboard.
    *   Smart Doctor Recommendation.

**Slide 4: Technology Stack**
*   **Backend:** Python, FastAPI, SQLAlchemy.
*   **Database:** MySQL (MariaDB).
*   **AI Engine:** Google Gemini Pro/Flash (Generative AI).
*   **Frontend:** HTML5, Bootstrap 5, Jinja2 Templates.

**Slide 5: System Architecture**
*   **Diagram:** [User] -> [Frontend UI] -> [FastAPI Server] -> [Gemini API] & [MySQL DB].
*   **Flow:** User submits data -> AI processes it -> Results stored -> Dashboard updated.

**Slide 6: Key Feature - AI Analysis**
*   **Capability:** Multimodal input (Text + Images).
*   **Output:** Diagnosis hypothesis, severity assessment, home remedies.
*   **differentiation:** Detailed medical context vs. simple keyword matching.

**Slide 7: Key Feature - Dashboard & History**
*   **Function:** Long-term health tracking.
*   **Details:** View past reports, generate AI summaries of complex reports for quick reading.
*   **Visual:** Screenshot of Dashboard Table.

**Slide 8: Key Feature - Finding Care**
*   **Feature:** "Find Doctor Nearby".
*   **Mechanism:** AI extracts specialist type -> Google Maps Search with location context.
*   **Benefit:** Actionable next steps, not just information.

**Slide 9: Future Enhancements**
*   **Roadmap:**
    *   Real-time chat interface.
    *   Appointment booking integration.
    *   Mobile Application (React Native).

**Slide 10: Conclusion**
*   **Summary:** MediBot delivers fast, accurate, and actionable health insights.
*   **Impact:** Empowers users to make informed health decisions.
*   **Q&A:** Open for questions.

---

### 3. Project Report

**Title:** Development of MediBot: An AI-Powered Medical Consultation System

**1. Introduction**
In an era where digital health solutions are becoming paramount, MediBot serves as a crucial first line of inquiry for patients. This project aims to develop a web-based application that leverages Large Language Models (LLMs) to understand patient symptoms and provide preliminary assessments.

**2. Objectives**
*   To implement a secure user authentication system.
*   To integrate Generative AI for analyzing textual symptoms and medical images.
*   To create a persistent storage system for patient medical history.
*   To provide location-based recommendations for healthcare providers.

**3. System Analysis and Design**
*   **Requirements:** The system requires a high-throughput backend (FastAPI) to handle concurrent API requests. Data integrity is managed via a Relational Database (MySQL).
*   **Database Schema:** Two primary entities were modeled: `Users` (storing credentials and profile) and `MedicalHistory` (storing consultation records, AI responses, and summaries).
*   **UI Design:** A modern, mobile-responsive interface was prioritized using Glassmorphism design principles to instill a sense of clean, modern healthcare tech.

**4. Implementation Details**
*   **Backend Logic:** The core logic resides in `main.py`, orchestrating routing and database sessions. `gemini_service.py` handles the interface with Google's Gemini API, utilizing custom prompts to ensure safe and structured medical advice.
*   **Data Handling:** Image uploads are handled via `Pillow`, saved locally, and their paths stored in the DB.
*   **Security:** Passwords are hashed using `pbkdf2_sha256`. User sessions are managed via secure HTTP-only cookies.

**5. Results and Discussion**
The application successfully handles end-to-end user flows:
*   Users can register and login.
*   Symptom analysis takes < 5 seconds on average.
*   The "Find Doctor" feature accurately identifies the correct specialist type (e.g., Dermatologist for skin issues) and generates valid map links.

**6. Conclusion**
MediBot successfully demonstrates the potential of integrating GenAI into primary healthcare workflows. By providing instant, 24/7 analysis and connecting patients to real-world doctors, it reduces medical anxiety and streamlines the path to care.

---

### 4. Project Video Script (5-7 Minutes)

**[0:00 - 0:45] Intro**
*   **Visual:** Title Screen, then cut to Speaker (or Screen Recording of Home Page).
*   **Audio:** "Hello everyone. Today I am excited to present MediBot, an intelligent medical assistant designed to provide immediate health insights. In a world where getting a doctor's appointment can take days, MediBot offers a preliminary analysis in seconds."

**[0:45 - 2:00] Architecture & Tech Stack**
*   **Visual:** Slide showing Tech Stack (FastAPI, MySQL, Gemini).
*   **Audio:** "We built this using FastAPI for its speed and efficiency. The brain of the operation is Google's Gemini AI, capable of understanding complex medical descriptions and even analyzing images. All user data is securely stored in a MySQL database."

**[2:00 - 3:30] Live Demo: Registration & Analysis**
*   **Visual:** Screen recording. User registering, then typing "I have a severe headache and sensitivity to light."
*   **Audio:** "Let's dive into a demo. Here I am creating a profile. Now, I'll enter some symptoms. I can also upload an image if I had a visible condition. I hit 'Analyze', and within moments... here is the result. It suggests it might be a migraine and recommends resting in a dark room."

**[3:30 - 5:00] Live Demo: Dashboard & Doctor Search**
*   **Visual:** Converting to Dashboard. Showing the table. Clicking "Generate Summary". Clicking "View Report".
*   **Audio:** "All these visits are saved in the Dashboard. Notice the 'Generate Summary' button—this uses AI to condense long reports into 2 sentences. Now, if I need real help, I click 'Find Doctor Nearby'. The system knows I have a migraine and am in [Location], so it automatically searches for Neurologists near me."

**[5:00 - 6:00] Code Walkthrough (Optional)**
*   **Visual:** VS Code showing `main.py` and `gemini_service.py`.
*   **Audio:** "A quick look under the hood. Here is our Gemini service handler where we engineer the prompts for safety and accuracy. And here is our database model."

**[6:00 - 6:30] Conclusion**
*   **Visual:** Home Page / Closing Slide.
*   **Audio:** "That is MediBot. A secure, smart, and helpful companion for your health journey. Thank you for watching."
