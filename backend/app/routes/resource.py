"""
Resource routes.
"""

from fastapi import APIRouter
from app.controllers.resource_controller import get_resources

router = APIRouter(prefix="/resources", tags=["Resources"])


@router.get("")
def list_resources():
    """GET /resources — get hospital resources."""
    return get_resources()
