from infrastructure.utilities import base, extensions
from infrastructure.page_objects import login_page, pim_page


def get_record_found_value():
    full_line = extensions.get_text(pim_page.records_found)
    splited_line = full_line.split('(')
    splited_partial_line = splited_line[1].split(')')
    value = splited_partial_line[0]
    return value
