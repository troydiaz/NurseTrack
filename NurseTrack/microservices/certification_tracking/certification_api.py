import requests

BASE_URL = "http://127.0.0.1:8001"  # Certification microservice runs on a different port

def add_certification(cert_id, name, issue_date, expiry_date):
    """Add a new certification."""
    response = requests.post(f"{BASE_URL}/certification", params={
        "id": cert_id,
        "name": name,
        "issue_date": issue_date,
        "expiry_date": expiry_date,
    })
    return response.json()

def get_certifications():
    """Retrieve all certifications."""
    response = requests.get(f"{BASE_URL}/certification")
    return response.json()

def get_expiring_certifications(days):
    """Retrieve certifications expiring within a given number of days."""
    response = requests.get(f"{BASE_URL}/certification/expiring", params={"days": days})
    return response.json()

def delete_certification(cert_id):
    """Delete a certification."""
    response = requests.delete(f"{BASE_URL}/certification/{cert_id}")
    return response.json()
