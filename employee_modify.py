from employee_io import save_employee

def modify_employee(emp_dict):
    emp_id = input("Enter the ID of the employee to modify: ")

    if emp_id not in emp_dict:
        print("Employee ID not found.")
        return

    employee = emp_dict[emp_id]

    while True:
        print("\nWhat would you like to modify?")
        print("[1] Name")
        print("[2] Role")
        print("[3] Salary")
        print("[4] Full-time status")
        print("[5] Done")

        choice = input("Enter your choice: ")
        if choice == "1":
            employee["name"] = input("Enter new name: ")
        elif choice == "2":
            employee["role"] = input("Enter new role: ")
        elif choice == "3":
            employee["salary"] = input("Enter new salary: ")
        elif choice == "4":
            ft = input("Full time Y/N: ").lower()
            employee["full_time"] = (ft == "y")

        elif choice == "5":
            break

        else:
            print("Invalid choice.")
            continue

        print("Field Updated")
    print(f"Employee {emp_id} updated successfully.")