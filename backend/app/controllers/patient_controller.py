"""
Patient controller — handles request logic and returns clean JSON responses.
"""

from app.services.patient_service import fetch_all_patients, fetch_patient
from app.utils.helpers import format_response


def get_patients():
    """Return all patients."""
    patients = fetch_all_patients()
    if patients:
        return format_response(True, patients, f"Fetched {len(patients)} patients")
    return format_response(False, [], "No patients found")


def get_patient(patient_id: str):
    """Return a single patient by ID."""
    patient = fetch_patient(patient_id)
    if patient:
        return format_response(True, patient, f"Patient {patient_id} found")
    return format_response(False, None, f"Patient {patient_id} not found")
