from infrastructure.utilities import base, extensions
from infrastructure.page_objects import login_page, pim_page, add_employee


def get_record_found_value():
    full_line = extensions.get_text(pim_page.records_found)
    splited_line = full_line.split('(')
    splited_partial_line = splited_line[1].split(')')
    value = splited_partial_line[0]
    return value


def create_employee(first_name, last_name, employee_id):
    extensions.click(pim_page.btn_add)
    extensions.send_text(add_employee.txt_firstName, first_name)
    extensions.send_text(add_employee.txt_lastName, last_name)
    extensions.send_text(add_employee.txt_employee_id, employee_id)
    extensions.click(add_employee.btn_save)
