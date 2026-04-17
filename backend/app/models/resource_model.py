"""
Resource model — MongoDB document helpers.
"""

from app.config.db import resources_collection
from app.utils.helpers import serialize_doc, current_timestamp


def get_resources() -> dict:
    """Retrieve the single hospital resources document."""
    doc = resources_collection.find_one()
    return serialize_doc(doc) if doc else {}


def upsert_resources(resource: dict):
    """Insert or update the resources document."""
    resource["lastUpdated"] = current_timestamp()
    resources_collection.update_one(
        {},
        {"$set": resource},
        upsert=True,
    )


def update_resource_field(field: str, value):
    """Update a single resource field."""
    resources_collection.update_one(
        {},
        {"$set": {field: value, "lastUpdated": current_timestamp()}},
    )
