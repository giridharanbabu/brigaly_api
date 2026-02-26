from fastapi import FastAPI, UploadFile, File, HTTPException
from models import ReviewRequest, ReviewResponse
from engine import review_content
from nudenet import NudeDetector
import os
import uuid
import shutil

app = FastAPI(title="MCP Review Server (Gemini)")

detector = NudeDetector()

UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/review", response_model=ReviewResponse)
async def review(request: ReviewRequest):
    try:
        result = await review_content(
            request.title,
            request.content,
            request.type
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/nudity")
async def detect_nudity(file: UploadFile = File(...)):
    try:
        file_ext = file.filename.split(".")[-1]
        temp_filename = f"{uuid.uuid4()}.{file_ext}"
        temp_path = os.path.join(UPLOAD_DIR, temp_filename)

        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        print(f"File saved to {temp_path}")
        result = detector.detect(temp_path)

        os.remove(temp_path)

        return {
            "status": "success",
            "detections": result,
            "is_nsfw": len(result) > 0
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))