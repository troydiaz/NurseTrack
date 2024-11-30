import requests

BASE_URL = "http://127.0.0.1:8002"  # Microservice D runs on a different port

def add_task(task_id, description, priority, due_date):
    """Add a new task."""
    response = requests.post(f"{BASE_URL}/task", params={
        "id": task_id,
        "description": description,
        "priority": priority,
        "due_date": due_date,
    })
    return response.json()

def get_tasks():
    """Retrieve all tasks."""
    response = requests.get(f"{BASE_URL}/task")
    return response.json()

def delete_task(task_id):
    """Delete a task."""
    response = requests.delete(f"{BASE_URL}/task/{task_id}")
    return response.json()
