"""
Patient Data API

This API is developed for managing Patient data.
Mock data is used for testing purposes.
"""

from fastapi import FastAPI

from routes.patients import router as patients_router

# Create FastAPI application
app = FastAPI(
    title="Patient Data API",
    description="REST API for managing Patient data",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add routes
app.include_router(patients_router)

@app.get("/", tags=["Home"])
async def root():
    """API home page"""
    return {
        "message": "Welcome to Patient Data API",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "patients": "/patients",
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 