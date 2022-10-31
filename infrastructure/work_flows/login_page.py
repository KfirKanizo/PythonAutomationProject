from infrastructure.utilities import base, extensions
from infrastructure.page_objects import login_page, pim_page


def login(username, password):
    extensions.send_text(login_page.txt_username, username)  # insert username
    extensions.send_text(login_page.txt_password, password)  # insert password
    extensions.click(login_page.btn_submit)  # click submit button
