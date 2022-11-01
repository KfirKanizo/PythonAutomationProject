from infrastructure.utilities import extensions
from infrastructure.page_objects import create_forms, general
from configuration import config


def create_employee(first_name, last_name, employee_id):
    extensions.click(general.btn_add)
    extensions.send_text(create_forms.txt_firstName, first_name)
    extensions.send_text(create_forms.txt_lastName, last_name)
    extensions.clear_field(create_forms.txt_employee_id)
    extensions.send_text(create_forms.txt_employee_id, employee_id)
    extensions.upload_img(create_forms.btn_upload_img, config.avatar)
    extensions.click(create_forms.btn_save)
