"""
MongoDB connection using pymongo.
"""

from pymongo import MongoClient
from app.config.settings import MONGO_URL, DATABASE_NAME

client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)
db = client[DATABASE_NAME]

# Collections
patients_collection = db["patients"]
resources_collection = db["resources"]
alerts_collection = db["alerts"]


def get_db():
    """Return the database instance."""
    return db


def check_db_connection():
    """Check if the MongoDB server is reachable."""
    try:
        client.admin.command('ping')
        return True
    except Exception:
        return False
