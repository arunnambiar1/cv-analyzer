from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException
import numpy as np
import cv2


app = FastAPI(title="CV Analyzer API")
@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/analyze")
async def analyze_cv(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Only images (png, jpg, gif, etc.) are allowed."
        )

    contents = await file.read()
    arr = np.frombuffer(contents, np.uint8)   
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    if img is None:
        raise HTTPException(
            status_code=400,
            detail="Could not read the image file. Please ensure it's a valid image."
        )

    height = img.shape[0]
    width = img.shape[1]

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size_bytes": len(contents),
        "width": width,
        "height": height
    }

    