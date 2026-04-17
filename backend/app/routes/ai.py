"""
AI routes.
"""

from fastapi import APIRouter
from app.controllers.ai_controller import analyze
from app.schemas.alert_schema import AIAnalyzeRequest

router = APIRouter(prefix="/ai", tags=["AI"])


@router.post("/analyze")
def ai_analyze(body: AIAnalyzeRequest):
    """POST /ai/analyze — run Gemini-powered medical analysis."""
    return analyze(prompt=body.prompt, patient_id=body.patientId)
