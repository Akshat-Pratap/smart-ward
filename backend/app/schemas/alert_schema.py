"""
Pydantic schemas for Alert.
"""

from typing import Optional
from pydantic import BaseModel


class AlertSchema(BaseModel):
    alertId: str
    type: str  # CRITICAL, WARNING, SYSTEM
    message: str
    patientId: Optional[str] = None
    timestamp: str
    resolved: bool = False


class AIAnalyzeRequest(BaseModel):
    prompt: Optional[str] = None
    patientId: Optional[str] = None
