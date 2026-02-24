from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException

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
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size_bytes": len(contents)
    }