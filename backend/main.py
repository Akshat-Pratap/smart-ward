"""
Smart Ward — Intelligent Healthcare System
Entry point for the FastAPI application.
"""

import json
import os
import sys
 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socketio
from app.config.socket_manager import sio, sio_app

# ── Ensure the backend directory is on sys.path so `app.*` imports work ──
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from app.routes.patient import router as patient_router
from app.routes.resource import router as resource_router
from app.routes.alert import router as alert_router
from app.routes.ai import router as ai_router

from app.config.db import patients_collection, resources_collection, alerts_collection, check_db_connection
from app.services.simulation_service import start_simulation

# ── Create FastAPI app ──────────────────────────────────────────────────────
fastapi_app = FastAPI(
    title="Smart Ward — Intelligent Healthcare System",
    description="Simulated hospital backend with real-time monitoring, alerts, and Gemini AI integration.",
    version="1.0.0",
    redirect_slashes=False,
)

# Wrap FastAPI with Socket.io
app = socketio.ASGIApp(sio, fastapi_app)

# ── CORS middleware ─────────────────────────────────────────────────────────
fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
# ── Include routers ─────────────────────────────────────────────────────────
fastapi_app.include_router(patient_router)
fastapi_app.include_router(resource_router)
fastapi_app.include_router(alert_router)
fastapi_app.include_router(ai_router)

# ── Socket.io event handlers ─────────────────────────────────────────────────
@sio.event
async def connect(sid, environ):
    print(f"[Socket] Client connected: {sid}")


@sio.event
async def disconnect(sid):
    print(f"[Socket] Client disconnected: {sid}")


# ── Seed database on startup ───────────────────────────────────────────────
DATA_DIR = os.path.join(BASE_DIR, "app", "data")


def _load_json(filename: str):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


@fastapi_app.on_event("startup")
def startup_event():
    """Seed MongoDB with initial data and start the simulation engine."""
    print("[Startup] Checking database connection...")
    
    if not check_db_connection():
        print("[Startup] WARNING: Could not connect to MongoDB. Skipping seeding and simulation.")
        print("[Startup] Please ensure MongoDB is running at localhost:27017")
        return

    print("[Startup] Seeding database...")

    # Seed patients
    if patients_collection.count_documents({}) == 0:
        patients = _load_json("patients.json")
        patients_collection.insert_many(patients)
        print(f"[Startup] Inserted {len(patients)} patients")
    else:
        print("[Startup] Patients collection already populated — skipping seed")

    # Seed resources
    if resources_collection.count_documents({}) == 0:
        resources = _load_json("resources.json")
        resources_collection.insert_one(resources)
        print("[Startup] Inserted resource data")
    else:
        print("[Startup] Resources collection already populated — skipping seed")

    # Seed alerts
    if alerts_collection.count_documents({}) == 0:
        alerts = _load_json("alerts.json")
        alerts_collection.insert_many(alerts)
        print(f"[Startup] Inserted {len(alerts)} alerts")
    else:
        print("[Startup] Alerts collection already populated — skipping seed")

    # Start simulation engine
    start_simulation()
    print("[Startup] Simulation engine started ✓")


# ── Health-check root endpoint ──────────────────────────────────────────────
@fastapi_app.get("/", tags=["Health"])
def root():
    return {
        "success": True,
        "message": "Smart Ward API is running 🏥",
        "docs": "/docs",
    }
