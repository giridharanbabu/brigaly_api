import os
import json
import re
import google.generativeai as genai
from models import ReviewResponse
from prompts import build_prompt

# Configure Gemini API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

MODEL_NAME = "gemini-2.5-flash"  # Use the latest Gemini Pro model
async def review_content(title: str, content: str, content_type: str) -> ReviewResponse:
    prompt = build_prompt(title, content, content_type)

    model = genai.GenerativeModel(MODEL_NAME)

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.2,
            "response_mime_type": "application/json"
        }
    )

    raw_text = response.text

    # Extract JSON safely (defensive parsing)
    match = re.search(r"\{.*\}", raw_text, re.DOTALL)
    if not match:
        raise ValueError(f"Invalid JSON from Gemini:\n{raw_text}")

    parsed = json.loads(match.group())

    return ReviewResponse(**parsed)