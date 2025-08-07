"""
Patient endpoints

API endpoints for managing patient data.
"""

from typing import List
from datetime import datetime
from fastapi import APIRouter, HTTPException, status

from models.patient import Patient
from data.mock_data import mock_patients

router = APIRouter(prefix="/patients", tags=["Patients"])


@router.get("/", response_model=List[Patient])
async def get_patients():
    """List all patients"""
    return mock_patients


@router.get("/{patient_id}", response_model=Patient)
async def get_patient(patient_id: str):
    """Get patient by ID"""
    for patient in mock_patients:
        if patient.id == patient_id:
            return patient
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Patient with ID {patient_id} not found"
    )


@router.post("/", response_model=Patient, status_code=status.HTTP_201_CREATED)
async def create_patient(patient: Patient):
    """Create new patient"""
    # ID check
    for existing_patient in mock_patients:
        if existing_patient.id == patient.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"ID {patient.id} already exists"
            )
    
    # Birth year control
    current_year = datetime.now().year
    if patient.birth_year > current_year:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Birth year cant be in the future"
        )
    
    mock_patients.append(patient)
    return patient
