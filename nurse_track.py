# Import the necessary helper functions
from microservices.work_schedule.work_schedule_api import add_schedule, get_schedules, delete_schedule
from microservices.certification_tracking.certification_api import (
    add_certification, get_certifications, get_expiring_certifications, delete_certification
)
from microservices.patient_tasks.patient_task_api import (
    add_task, get_tasks, delete_task
)

def schedule_menu():
    """Menu for managing work schedules."""
    while True:
        print("\nWork Schedule Management:")
        print("1. Add Schedule")
        print("2. View Schedules")
        print("3. Delete Schedule")
        print("4. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == "1":
            # Add a schedule
            schedule_id = int(input("Enter Schedule ID: "))
            date = input("Enter Date (YYYY-MM-DD): ")
            shift = input("Enter Shift (e.g., Morning, Evening): ")
            response = add_schedule(schedule_id, date, shift)
            print("Response:", response)

        elif choice == "2":
            # View all schedules
            schedules = get_schedules()
            print("Schedules:", schedules)

        elif choice == "3":
            # Delete a schedule
            schedule_id = int(input("Enter Schedule ID to Delete: "))
            response = delete_schedule(schedule_id)
            print("Response:", response)

        elif choice == "4":
            # Exit the schedule menu
            break

        else:
            print("Invalid option. Please try again.")

def certification_menu():
    """Menu for managing certifications."""
    while True:
        print("\nCertification Management:")
        print("1. Add Certification")
        print("2. View All Certifications")
        print("3. View Expiring Certifications")
        print("4. Delete Certification")
        print("5. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == "1":
            cert_id = int(input("Enter Certification ID: "))
            name = input("Enter Certification Name: ")
            issue_date = input("Enter Issue Date (YYYY-MM-DD): ")
            expiry_date = input("Enter Expiry Date (YYYY-MM-DD): ")
            print(add_certification(cert_id, name, issue_date, expiry_date))

        elif choice == "2":
            print(get_certifications())

        elif choice == "3":
            days = int(input("Enter number of days to check for expiring certifications: "))
            print(get_expiring_certifications(days))

        elif choice == "4":
            cert_id = int(input("Enter Certification ID to Delete: "))
            print(delete_certification(cert_id))

        elif choice == "5":
            break

        else:
            print("Invalid option. Please try again.")

def task_menu():
    """Menu for managing patient care tasks."""
    while True:
        print("\nPatient Care Task Management:")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Delete Task")
        print("4. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == "1":
            task_id = int(input("Enter Task ID: "))
            description = input("Enter Task Description: ")
            priority = input("Enter Task Priority (e.g., High, Medium, Low): ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ")
            print(add_task(task_id, description, priority, due_date))

        elif choice == "2":
            print(get_tasks())

        elif choice == "3":
            task_id = int(input("Enter Task ID to Delete: "))
            print(delete_task(task_id))

        elif choice == "4":
            break

        else:
            print("Invalid option. Please try again.")

def main_menu():
    """Main menu for NurseTrack."""
    while True:
        print("\nNurseTrack Main Menu:")
        print("1. Manage Work Schedules")
        print("2. Manage Certifications")
        print("3. Manage Patient Care Tasks")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            # Open the schedule management menu
            schedule_menu()

        elif choice == "2":
            # Open the certification management menu
            certification_menu()

        elif choice == "3":
            # Open the task management menu
            task_menu()

        elif choice == "4":
            # Exit the program
            print("Exiting NurseTrack. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Program Entry Point
if __name__ == "__main__":
    main_menu()
