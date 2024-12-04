from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Dummy user database
users = {
    "diaztr": "CS361",
    "admin": "password123"
}

# Define a Pydantic model for the request body
class AuthRequest(BaseModel):
    username: str
    password: str

@app.post("/authenticate")
def authenticate(auth_request: AuthRequest):
    """Authenticate a user."""
    username = auth_request.username
    password = auth_request.password

    if username in users and users[username] == password:
        return {"authenticated": True, "message": "Access granted"}
    return {"authenticated": False, "message": "Invalid credentials"}
