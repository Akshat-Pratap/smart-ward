"""
Resource controller — handles request logic for hospital resources.
"""

from app.services.resource_service import fetch_resources
from app.utils.helpers import format_response


def get_resources():
    """Return current hospital resources."""
    resources = fetch_resources()
    if resources:
        return format_response(True, resources, "Hospital resources fetched")
    return format_response(False, {}, "No resource data available")
