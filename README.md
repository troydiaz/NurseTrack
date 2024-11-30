* Requirements
* ------------
* Install Python 3.9 or higher
* Required Python Libraries: fastapi, uvicorn, requests
* 
* pip install fastapi uvicorn requests
*
* Run each microservice:
* ------------
* Microservice A - Password Authentication
* cd microservices/password_auth
* uvicorn main:app --reload --port 8003
*
* Microservice B - Work Schedule Management
* cd microservices/work_schedule
* uvicorn main:app --reload --port 8000
*
* Microservice C - Certification Tracking
* cd microservices/certification_tracking
* uvicorn main:app --reload --port 8001
*
* Microservice D - Patient Care Task Management
* cd microservices/patient_tasks
* uvicorn main:app --reload --port 8002
*
* Run the Main Program:
* ------------
* cd NurseTrack
* python3 nurse_track.py
*
* Using the Program:
* ------------
* 1. Log in with your credentials:
*    - Default credentials:
*      - Username: diaztr
*      - Password: CS361
*
* 2. Choose from the available options in the main menu:
*    - Manage Work Schedules
*    - Manage Certifications
*    - Manage Patient Care Tasks
*    - Exit
*
* Default Ports Used by Microservices:
* ------------
* - Microservice A (Password Authentication): Port 8003
* - Microservice B (Work Schedule Management): Port 8000
* - Microservice C (Certification Tracking): Port 8001
* - Microservice D (Patient Care Task Management): Port 8002
