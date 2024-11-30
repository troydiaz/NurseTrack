from fastapi import FastAPI, HTTPException
from datetime import datetime, timedelta

app = FastAPI()

certifications = {}

@app.post("/certification")
def add_certification(id: int, name: str, issue_date: str, expiry_date: str):
    """Add a new certification."""
    if id in certifications:
        raise HTTPException(status_code=400, detail=f"Certification with ID {id} already exists.")
    certifications[id] = {
        "name": name,
        "issue_date": issue_date,
        "expiry_date": expiry_date,
    }
    return {"message": "Certification added successfully"}

@app.get("/certification")
def get_certifications():
    """Retrieve all certifications."""
    return certifications

@app.get("/certification/expiring")
def get_expiring_certifications(days: int = 30):
    """Retrieve certifications expiring within a specified number of days."""
    today = datetime.now()
    expiring = {
        id: cert
        for id, cert in certifications.items()
        if datetime.strptime(cert["expiry_date"], "%Y-%m-%d") <= today + timedelta(days=days)
    }
    return expiring

@app.delete("/certification/{id}")
def delete_certification(id: int):
    """Delete a certification."""
    if id not in certifications:
        raise HTTPException(status_code=404, detail="Certification not found")
    del certifications[id]
    return {"message": "Certification deleted successfully"}
