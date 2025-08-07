"""
API Test File

This file is used to test the basic functions of the API.
"""

import requests
import json

# API base URL
BASE_URL = "http://localhost:8000"

def test_root_endpoint():
    """Test home page endpoint"""
    print("Testing root endpoint")
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    print("Root endpoint test passed")

def test_get_patients():
    """Test patient list endpoint"""
    print("Testing get patients endpoint")
    response = requests.get(f"{BASE_URL}/patients")
    assert response.status_code == 200
    patients = response.json()
    assert isinstance(patients, list)
    assert len(patients) > 0
    print(f"Get patients test passed - {len(patients)} patients found")

def test_get_patient_by_id():
    """Test get patient by ID endpoint"""
    print("Testing get patient by ID endpoint")
    patient_id = "PAT001"
    response = requests.get(f"{BASE_URL}/patients/{patient_id}")
    assert response.status_code == 200
    patient = response.json()
    assert patient["id"] == patient_id
    print(f"Get patient by ID test passed - {patient['name']}")

def test_create_patient():
    """Test create new patient endpoint"""
    print("Testing create patient endpoint")
    new_patient = {
        "id": "PAT_TEST",
        "name": "Test Patient New",
        "birth_year": 1995,
        "variants": []
    }
    response = requests.post(
        f"{BASE_URL}/patients",
        json=new_patient,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 201
    created_patient = response.json()
    assert created_patient["id"] == new_patient["id"]
    print("Create patient test passed")

def test_error_handling():
    """Test error conditions"""
    print("Testing error handling")
    
    # Non-existent patient ID
    response = requests.get(f"{BASE_URL}/patients/NONEXISTENT")
    assert response.status_code == 404
    
    print("Error 404 test passed")

def run_all_tests():
    """Run all tests"""
    print("Starting API test\n")
    
    try:
        test_root_endpoint()
        test_get_patients()
        test_get_patient_by_id()
        test_create_patient()
        test_error_handling()
        
        print("\n All tests passed successfully!")
        
    except requests.exceptions.ConnectionError:
        print("Error connect to API")
    except Exception as e:
        print(f"Test failed: {str(e)}")

if __name__ == "__main__":
    run_all_tests() 