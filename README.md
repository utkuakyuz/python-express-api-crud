# Patient Data API

This project is a very simple REST API application developed for managing Patient data and variant information. It is built using the FastAPI framework for personel learning purposes.

## Features

- **Patient Management**: List, view, and add patient information
- **Swagger UI**: Automatic API documentation (`/docs`)
- **Pydantic Models**: Data validation and serialization
- **Mock Data**: Sample data for testing purposes
- **Virtual Environment**: Isolated dependency management for the project

## Technologies

- Python 3.10+
- FastAPI 0.104.1
- Pydantic 2.5.0
- Uvicorn 0.24.0
- Requests 2.31.0 (for testing)

## Prerequisites

### Python Installation

This project requires Python 3.10 or higher

## Installation

1. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```
## Running

### Starting the API

With the virtual environment active start the API:

```bash
# Activate virtual environment (if not active)
venv\Scripts\activate 

# Start the API
python main.py
```

or

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will run at: `http://localhost:8000`

### Running Tests

```bash
# First run the API then
# Open a new terminal and run tests
venv\Scripts\activate  # Activate virtual environment
python test_api.py
```

## API Endpoints

### Home
- `GET /` - API information

### Patients
- `GET /patients` - List all patients
- `GET /patients/{patient_id}` - Get patient by ID
- `POST /patients` - Create new patient

## API Documentation

To access API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Code Structure

- **models/**: Pydantic models and data schemas
- **data/**: Mock data and data management
- **routes/**: API endpoints and routes
- **main.py**: Main application file
