import os
from fastapi import FastAPI, UploadFile,File,HTTPException
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    raw = await file.read()
    try:
        content = raw.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(status_code=400,detail="Please upload a text file")

    return {
        "characters": len(content),
        "words": len(content.split()),
        "lines": len(content.splitlines()),
    }
if os.path.isdir("public"):
    app.mount("/", StaticFiles(directory="public", html=True), name="static")