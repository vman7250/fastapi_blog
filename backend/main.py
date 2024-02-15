from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

@app.get("/")
def Hello():
    return {"msg":"Hello FastAPI"}
    