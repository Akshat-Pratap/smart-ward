"""
Patient routes.
"""

from fastapi import APIRouter
from app.controllers.patient_controller import get_patients, get_patient

router = APIRouter(prefix="/patients", tags=["Patients"])


@router.get("")
def list_patients():
    """GET /patients — list all patients."""
    return get_patients()


@router.get("/{patient_id}")
def retrieve_patient(patient_id: str):
    """GET /patients/{patient_id} — get a single patient."""
    return get_patient(patient_id)
