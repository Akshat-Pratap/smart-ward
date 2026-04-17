"""
Resource service — business logic for hospital resource operations.
"""

from app.models.resource_model import (
    get_resources,
    upsert_resources,
    update_resource_field,
)


def fetch_resources() -> dict:
    """Return current hospital resources."""
    try:
        return get_resources()
    except Exception as e:
        print(f"[ResourceService] Error fetching resources: {e}")
        return {}


def save_resources(resource: dict):
    """Create or update resources."""
    try:
        upsert_resources(resource)
    except Exception as e:
        print(f"[ResourceService] Error saving resources: {e}")


def update_icu_stats(icu_occupied: int):
    """Update ICU occupied count and recalculate availability."""
    try:
        resources = get_resources()
        icu_beds = resources.get("icuBeds", 20)
        icu_occupied = max(0, min(icu_beds, icu_occupied))
        update_resource_field("icuOccupied", icu_occupied)
        update_resource_field("icuAvailable", icu_beds - icu_occupied)
    except Exception as e:
        print(f"[ResourceService] Error updating ICU stats: {e}")
