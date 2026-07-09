"""
This is the entry point of the backend.
Running `uvicorn app.main:app --reload` starts this file.

Today we are only wiring up the app itself - no real features
(tools, categories, search) yet. Just proving frontend <-> backend
<-> database can all talk to each other.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

app = FastAPI(
    title="AI Tools Directory API",
    version="0.1.0",
)

# CORS lets the Next.js frontend (running on a different port/domain)
# call this API from the browser. Without this, the browser blocks
# the requests for security reasons.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "AI Tools Directory API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


# Future routers will be added here, e.g.:
# from app.routes import tools, categories
# app.include_router(tools.router, prefix="/api/v1/tools", tags=["tools"])
# app.include_router(categories.router, prefix="/api/v1/categories", tags=["categories"])
