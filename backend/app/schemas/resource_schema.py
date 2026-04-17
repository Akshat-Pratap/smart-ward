"""
Pydantic schemas for Resource.
"""

from typing import Optional
from pydantic import BaseModel


class ResourceSchema(BaseModel):
    totalBeds: int
    occupiedBeds: int
    availableBeds: int
    icuBeds: int
    icuOccupied: int
    icuAvailable: int
    ventilators: int
    ventilatorsInUse: int
    oxygenCylinders: int
    oxygenInUse: int
    emergencyBeds: int
    emergencyOccupied: int
    operatingRooms: int
    orInUse: int
    wheelchairs: int
    wheelchairsInUse: int
    lastUpdated: Optional[str] = None


class ResourceUpdateSchema(BaseModel):
    icuOccupied: Optional[int] = None
    occupiedBeds: Optional[int] = None
    ventilatorsInUse: Optional[int] = None
    oxygenInUse: Optional[int] = None
    emergencyOccupied: Optional[int] = None
    orInUse: Optional[int] = None
