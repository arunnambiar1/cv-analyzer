from fastapi import FastAPI

app = FastAPI(title="CV Analyzer API")
@app.get("/")
def health():
    return {"statsus": "ok"}
