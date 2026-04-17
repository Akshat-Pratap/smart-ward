"""
Application settings — loads secrets from environment variables.
"""

import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL: str = os.getenv("MONGO_URL", "mongodb://localhost:27017")
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
DATABASE_NAME: str = "smart_ward"
