"""
Utility helpers — random generators and formatting.
"""

import random
import string
from datetime import datetime, timezone


def random_vital_fluctuation(value: int, low: int, high: int, delta: int = 5) -> int:
    """Randomly adjust a vital sign within bounds."""
    change = random.randint(-delta, delta)
    new_value = value + change
    return max(low, min(high, new_value))


def generate_alert_id() -> str:
    """Generate a unique alert ID."""
    suffix = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"A-{suffix}"


def current_timestamp() -> str:
    """Return current UTC timestamp as ISO string."""
    return datetime.now(timezone.utc).isoformat()


def format_response(success: bool, data=None, message: str = "") -> dict:
    """Standard API response envelope."""
    return {
        "success": success,
        "data": data,
        "message": message,
    }


def serialize_doc(doc: dict) -> dict:
    """Convert MongoDB document to JSON-serialisable dict (handles ObjectId)."""
    if doc is None:
        return {}
    doc = dict(doc)
    if "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc


def serialize_docs(docs) -> list:
    """Serialise a list / cursor of MongoDB documents."""
    return [serialize_doc(d) for d in docs]
