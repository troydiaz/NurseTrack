from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = {}

@app.post("/task")
def add_task(id: int, description: str, priority: str, due_date: str):
    """Add a new task."""
    if id in tasks:
        raise HTTPException(status_code=400, detail=f"Task with ID {id} already exists.")
    tasks[id] = {
        "description": description,
        "priority": priority,
        "due_date": due_date,
    }
    return {"message": "Task added successfully"}

@app.get("/task")
def get_tasks():
    """Retrieve all tasks."""
    return tasks

@app.delete("/task/{id}")
def delete_task(id: int):
    """Delete a task by its ID."""
    if id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[id]
    return {"message": "Task deleted successfully"}
