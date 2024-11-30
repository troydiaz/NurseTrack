from fastapi import FastAPI, HTTPException

app = FastAPI()

# Dummy user database
users = {
    "diaztr": "CS361",
    "admin": "password123"
}

@app.post("/authenticate")
def authenticate(username: str, password: str):
    """Authenticate a user."""
    if username in users and users[username] == password:
        return {"authenticated": True, "message": "Access granted"}
    return {"authenticated": False, "message": "Invalid credentials"}
