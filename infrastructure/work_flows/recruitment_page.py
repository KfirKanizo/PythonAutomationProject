from infrastructure.utilities import extensions
from infrastructure.page_objects import general, create_forms


def create_candidate(first_name, last_name, vacancy, email, resume, date):
    extensions.click(general.btn_add)
    extensions.send_text(create_forms.txt_firstName, first_name)
    extensions.send_text(create_forms.txt_lastName, last_name)
    extensions.click(create_forms.btn_vacancy)
    extensions.select_drop_down_by_text(create_forms.dd_vacancy_select, vacancy)
    extensions.send_text(create_forms.txt_email, email)
    extensions.send_text(create_forms.btn_upload_resume, resume)
    extensions.send_text(create_forms.date, date)
    extensions.click(create_forms.btn_save)
