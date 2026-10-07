import json

def load_employees():
    with open("employee_list.json", "r") as f:
        return json.load(f)

def save_employee(emp_dict):
    with open("employee_list.json", "w") as f:
        json.dump(emp_dict, f, indent=4)

def load_archived():
    with open("employee_archive.json", "r") as f:
        return json.load(f)

def save_archived(archived_dict):
    with open("employee_archive.json", "w") as f:
        json.dump(archived_dict, f, indent=4)
