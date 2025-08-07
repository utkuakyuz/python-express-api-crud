"""
Patient model

Pydantic model representing patient information.
"""

from typing import List
from datetime import datetime
from pydantic import BaseModel, Field

class Patient(BaseModel):
    """Patient model"""
    id: str = Field(..., description="Patient unique identifier")
    name: str = Field(..., description="Patient name")
    birth_year: int = Field(..., ge=1900, le=2024, description="Birth year")
    variants: List[str] = Field(default=[], description="Variants detected in the patient")
    created_at: datetime = Field(default_factory=datetime.now, description="Record creation date")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "PAT001",
                "name": "Test Patient Name",
                "birth_year": 1985,
                "variants": [],
                "created_at": "2024-01-15T10:30:00"
            }
        } 