"""
AI controller — handles request logic for Gemini-powered analysis.
"""

from app.services.ai_service import analyze_with_gemini, build_patient_prompt
from app.services.patient_service import fetch_patient
from app.utils.helpers import format_response


def analyze(prompt: str | None = None, patient_id: str | None = None):
    """
    Run AI analysis.

    If a patientId is provided, build a prompt from that patient's data.
    Otherwise, use the raw prompt string.
    """
    # Build prompt from patient data if patientId is given
    if patient_id:
        patient = fetch_patient(patient_id)
        if not patient:
            return format_response(False, None, f"Patient {patient_id} not found")
        prompt = build_patient_prompt(patient)
    elif not prompt:
        return format_response(False, None, "Provide either a 'prompt' or a 'patientId'")

    # Call Gemini
    result = analyze_with_gemini(prompt)

    return format_response(True, {"analysis": result, "prompt_used": prompt}, "AI analysis complete")
