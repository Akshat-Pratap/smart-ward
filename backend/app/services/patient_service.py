"""
Patient service — business logic for patient operations.
"""

from app.models.patient_model import (
    get_all_patients,
    get_patient_by_id,
    upsert_patient,
    update_patient_vitals,
    update_patient_status,
)


def fetch_all_patients() -> list:
    """Return every patient from the database."""
    try:
        return get_all_patients()
    except Exception as e:
        print(f"[PatientService] Error fetching patients: {e}")
        return []


def fetch_patient(patient_id: str) -> dict | None:
    """Return a single patient by ID."""
    try:
        return get_patient_by_id(patient_id)
    except Exception as e:
        print(f"[PatientService] Error fetching patient {patient_id}: {e}")
        return None


def save_patient(patient: dict):
    """Create or update a patient record."""
    try:
        upsert_patient(patient)
    except Exception as e:
        print(f"[PatientService] Error saving patient: {e}")


def set_patient_vitals(patient_id: str, vitals: dict):
    """Update vitals for a specific patient."""
    try:
        update_patient_vitals(patient_id, vitals)
    except Exception as e:
        print(f"[PatientService] Error updating vitals for {patient_id}: {e}")


def set_patient_status(patient_id: str, status: str):
    """Update status for a specific patient."""
    try:
        update_patient_status(patient_id, status)
    except Exception as e:
        print(f"[PatientService] Error updating status for {patient_id}: {e}")
