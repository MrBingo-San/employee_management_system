def view_employee(emp_dict):
    if not emp_dict:
        print("Employee not found")
        return
    print("\n --- Employee List ---")
    for emp_id in emp_dict.keys():
        print(f"Employee ID: {emp_id}")
        print(f"  Name: {emp_dict[emp_id]['name']}")
        print(f"  Role: {emp_dict[emp_id]['role']}")
        print(f"  Salary: {emp_dict[emp_id]['salary']}")
        print(f"  Full Time: {"Yes" if emp_dict[emp_id]['full_time'] else "No"}")
        print("-" * 25)