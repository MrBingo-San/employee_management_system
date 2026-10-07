from employee_io import load_employees
from employee_add import add_employee
from employee_view import view_employee
from employee_archive import remove_employee
from employee_modify import modify_employee


employees = load_employees()

while True:
    choice = input("""Choose an option: 
    [A]dd
    [V]iew
    [R]emove 
    [M]odify
    [Q]uit
    """).lower()
    if choice == "a":
        add_employee(employees)
    elif choice == "v":
        view_employee(employees)
    elif choice == "r":
        remove_employee(employees)
    elif choice == "m":
        modify_employee(employees)
    elif choice == "q":
        break
    else:
        print("Invalid option")