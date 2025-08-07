"""
Mock data

Mock data for API testing purposes.
"""

from models.patient import Patient

# Mock patient data
mock_patients = [
    Patient(
        id="PAT001",
        name="Test Patient Ahmet",
        birth_year=1985,
        variants=["Benign","Likely Pathogenic"]
    ),
    Patient(
        id="PAT002", 
        name="Test Patient Ayşe Demir",
        birth_year=1992,
        variants=["Pathogenic"]
    ),
    Patient(
        id="PAT003",
        name="Test Patient Mehmet", 
        birth_year=1978,
        variants=[]
    )
] 