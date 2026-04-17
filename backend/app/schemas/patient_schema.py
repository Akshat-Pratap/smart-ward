"""
Pydantic schemas for Patient.
"""

from typing import Optional
from pydantic import BaseModel


class VitalsSchema(BaseModel):
    heartRate: int
    oxygen: int
    bpSystolic: int
    bpDiastolic: int


class PatientSchema(BaseModel):
    patientId: str
    name: str
    age: int
    gender: str
    ward: str
    bed: str
    diagnosis: str
    vitals: VitalsSchema
    status: str


class PatientUpdateSchema(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    ward: Optional[str] = None
    bed: Optional[str] = None
    diagnosis: Optional[str] = None
    vitals: Optional[VitalsSchema] = None
    status: Optional[str] = None
