import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# Use a model that supports vision if images are involved, e.g., gemini-1.5-flash
model = genai.GenerativeModel('gemini-flash-latest')

def analyze_symptoms(symptoms: str, weight: str = None, age: int = None, gender: str = None, image_path: str = None):
    prompt_parts = [
        "You are a medical AI assistant. Analyze the following patient details and symptoms.",
        f"Symptoms: {symptoms}",
    ]
    if weight:
        prompt_parts.append(f"Weight: {weight}")
    if age:
        prompt_parts.append(f"Age: {age}")
    if gender:
        prompt_parts.append(f"Gender: {gender}")

    prompt_parts.append("\nPlease provide:")
    prompt_parts.append("1. Potential causes.")
    prompt_parts.append("2. Possible Diseases/Conditions.")
    prompt_parts.append("3. Recommended next steps or home remedies (if applicable).")
    prompt_parts.append("IMPORTANT: Always include a disclaimer that you are an AI and this is not professional medical advice.")

    input_data = prompt_parts

    if image_path and os.path.exists(image_path):
        # Load image
        import PIL.Image
        img = PIL.Image.open(image_path)
        input_data.append(img)
    
    try:
        response = model.generate_content(input_data)
        return response.text
    except Exception as e:
        return f"Error connecting to Gemini API: {str(e)}"

def summarize_text(text: str):
    prompt = f"Please provide a concise, 2-3 sentence summary of the following medical analysis for a patient's dashboard preview:\n\n{text}"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error creating summary: {str(e)}"

def get_doctors_list(symptoms: str, location: str):
    prompt = f"""
    Act as a medical directory assistant.
    Based on the following symptoms: "{symptoms}" and location: "{location}", provide a list of 3 recommended types of specialists or doctors.
    For each, provide a fictional but realistic entry with:
    - Name
    - Clinic Name
    - Phone Number
    - Address near {location}
    
    Return ONLY a raw JSON array of objects. Do not use markdown formatting.
    Example format:
    [
        {{"name": "Dr. Smith", "clinic": "City Health", "phone": "555-0123", "address": "123 Main St, {location}"}}
    ]
    """
    try:
        response = model.generate_content(prompt)
        text = response.text
        # Clean up if markdown is present
        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "")
        return text.strip()
    except Exception as e:
        return "[]"
