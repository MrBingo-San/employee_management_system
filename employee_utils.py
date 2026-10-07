def get_next_id(emp_dict):
    if not emp_dict:
        return 1
    return max(int(emp_id) for emp_id in emp_dict.keys()) + 1