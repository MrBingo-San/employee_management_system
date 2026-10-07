from employee_io import save_employee
from employee_utils import get_next_id

def add_employee(emp_dict):
    while True:
        emp_id = get_next_id(emp_dict)

        name = input("Enter employee name: ")
        role = input("Enter employee role: ")
        salary = float(input("Enter employee salary: "))
        full_time = input("Full time (Y/N): ").lower() == "y"

        emp_dict[str(emp_id)] = {
            "name": name,
            "role": role,
            "salary": salary,
            "full_time": full_time,
        }

        save_employee(emp_dict)
        print(f"Employee added with ID {emp_id}")
        print()
        again = input("Add another employee? [Y]/N: ").lower()
        if again != "y":
            break