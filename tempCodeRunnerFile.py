from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
import os
import json
from google import genai
from google.genai import types

app = FastAPI()

# CORS Middleware for Frontend Connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔑 APNA GEMINI API KEY YAHAN DAALEIN
# Aap Google AI Studio se free key lekar yahan replace kar sakte hain
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "AQ.Ab8RN6JtQrAFOLlM6TbwwCigXV2F6xIApJjIZaGkfC9yTKeZHg")

# Initialize Gemini Client
try:
    client = genai.Client(api_key=GEMINI_API_KEY)
except Exception as e:
    print(f"Gemini Init Warning: {e}. API calls will fallback if key is missing.")

# Keep the mock pool for the live-feed simulation dashboard
NEWS_POOL = [
    {
        "id": 1, 
        "title": "Government announces new digital currency rules for 2026.", 
        "content": "The Ministry of Finance has officially introduced a streamlined taxation and legal framework for all digital assets starting this quarter. According to the official statement, this rule aims to secure digital transactions, prevent international fraud, and bring transparency to digital currency holding.", 
        "accuracy": 94
    },
    {
        "id": 2, 
        "title": "NASA's Rover finds clear evidence of ancient water streams on Mars.", 
        "content": "NASA's Perseverance rover has sent back stunning new soil and rock sample analysis reports from the Jezero Crater. The data indicates clear historical sedimentary rock formations that could only be shaped by deep, continuous ancient water streams billions of years ago.", 
        "accuracy": 98
    },
    {
        "id": 3, 
        "title": "UNESCO declares Indian National Anthem as the best in the world.", 
        "content": "A viral message on social media platforms claims that UNESCO has recently declared the Indian National Anthem, 'Jana Gana Mana', as the best national anthem in the world. No official website or press release from UNESCO mentions any such competitive broadcast or announcement.", 
        "accuracy": 12
    }
]

class NewsInput(BaseModel):
    text: str

@app.get("/api/live-feed")
def get_live_feed():
    shuffled = list(NEWS_POOL)
    random.shuffle(shuffled)
    return shuffled[:6]

@app.post("/api/verify-news")
def verify_news(data: NewsInput):
    # Fallback response in case AI fails or API key is not provided
    fallback_response = {
        "status": "Suspicious / Unverified",
        "score": 50,
        "description": "API Key is missing or invalid. Please configure GEMINI_API_KEY in In.py.",
        "explanation_1": "Could not contact AI detection engine for dynamic verification.",
        "explanation_2": "Please update your API credentials inside the backend script."
    }

    if not GEMINI_API_KEY or GEMINI_API_KEY == "YOUR_GEMINI_API_KEY_HERE":
        return fallback_response

    try:
        # Prompt telling Gemini exactly how to analyze and return data in strict JSON structure
        prompt = f"""
        Analyze the following news text for facts, rumors, fraud, or truth. 
        You must respond ONLY with a valid JSON object matching this exact structure:
        {{
            "status": "Real News" or "Suspicious / Misleading" or "Fake News / Fabricated",
            "score": <an integer between 0 and 100 representing truth probability>,
            "description": "<a short 1-sentence summary of your judgment>",
            "explanation_1": "<First factual reason or cross-reference check detail>",
            "explanation_2": "<Second structural or verification reason detail>"
        }}
        
        News Text to verify: "{data.text}"
        """

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json"
            )
        )
        
        # Parse the JSON response received from AI
        result = json.loads(response.text.strip())
        return result

    except Exception as e:
        print(f"Error calling AI Engine: {e}")
        return fallback_response

# In.py ke sabse niche ye line aise badal do:
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8050) # <-- 8000 ki jagah 8050 kar diya