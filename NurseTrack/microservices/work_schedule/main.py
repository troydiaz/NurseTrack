from fastapi import FastAPI, HTTPException

app = FastAPI()

schedules = {}

@app.post("/schedule")
def add_schedule(id: int, date: str, shift: str):
    if id in schedules:
        raise HTTPException(status_code=400, detail="Schedule already exists")
    schedules[id] = {"date": date, "shift": shift}
    return {"message": "Schedule added successfully"}

@app.get("/schedule")
def get_schedules(date: str = None):
    if date:
        return {id: schedule for id, schedule in schedules.items() if schedule["date"] == date}
    return schedules

@app.put("/schedule/{id}")
def update_schedule(id: int, date: str = None, shift: str = None):
    if id not in schedules:
        raise HTTPException(status_code=404, detail="Schedule not found")
    if date:
        schedules[id]["date"] = date
    if shift:
        schedules[id]["shift"] = shift
    return {"message": "Schedule updated successfully"}

@app.delete("/schedule/{id}")
def delete_schedule(id: int):
    if id not in schedules:
        raise HTTPException(status_code=404, detail="Schedule not found")
    del schedules[id]
    return {"message": "Schedule deleted successfully"}
