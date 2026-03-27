from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import review
from core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description="AI-powered code review assistant using Claude AI"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(review.router)

@app.get("/")
def home():
    return {
        "message": "Code Review Assistant API",
        "version": settings.version,
        "docs": "/docs"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}