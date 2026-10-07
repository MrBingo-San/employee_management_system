from employee_io import load_archived, save_archived, save_employee

def remove_employee(emp_dict):
    while True:
        emp_id = input("Enter the ID of the employee to remove: ")
        if emp_id not in emp_dict:
            print("Employee not found")
            return
        archived = load_archived()

        archived[emp_id] = emp_dict[emp_id]
        del emp_dict[emp_id]
        save_archived(archived)
        save_employee(emp_dict)
        print("Employee removed")
        again = input("Remove another employee Y/N: ").lower()
        if again != "y":
            break