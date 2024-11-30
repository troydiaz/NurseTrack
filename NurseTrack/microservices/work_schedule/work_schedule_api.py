import requests

BASE_URL = "http://127.0.0.1:8000"

def add_schedule(schedule_id, date, shift):
    """Add a new schedule to the microservice."""
    response = requests.post(f"{BASE_URL}/schedule", params={"id": schedule_id, "date": date, "shift": shift})
    return response.json()

def get_schedules():
    """Retrieve all schedules from the microservice."""
    response = requests.get(f"{BASE_URL}/schedule")
    return response.json()

def delete_schedule(schedule_id):
    """Delete a schedule by its ID."""
    response = requests.delete(f"{BASE_URL}/schedule/{schedule_id}")
    return response.json()
