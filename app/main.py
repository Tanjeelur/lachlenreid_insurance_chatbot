from fastapi import FastAPI
from app.api.v1.endpoints import analyze

app = FastAPI(title="Insurance AI API")

app.include_router(analyze.router, prefix="/api/v1/analyze", tags=["Analysis"])
