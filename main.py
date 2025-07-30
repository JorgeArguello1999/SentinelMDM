from fastapi import FastAPI
from auth.routes import router as auth_router

from dotenv import load_dotenv
from os import getenv
load_dotenv()

from pydantic import BaseModel
from fastapi import status, HTTPException

class ResponseModel(BaseModel):
    message: str

app = FastAPI(
    title = "Sentinel Backend API",
    description = "API for managing users, authentication, agents and others functions.",
    version = "0.1.0", # Update this version as needed
    contact = {
        "name": "JorgeArguello1999",
        "email": "contact@jorgearguello.net",
    },
    license_info = {
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    }
)

# Registering routes
app.include_router(auth_router, prefix="/auth", tags=["Auth"])

@app.get("/", tags=["Root"], response_model=ResponseModel, 
    responses={
        status.HTTP_200_OK: {"description": "Root endpoint"},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal Server Error"},
        status.HTTP_404_NOT_FOUND: {"description": "Not Found"}
    }
)
def read_root():
    return {"message": "Welcome to the FastAPI project!"}

# LOGs
print(f"DATABASE: {getenv('DATABASE_URL')}")

