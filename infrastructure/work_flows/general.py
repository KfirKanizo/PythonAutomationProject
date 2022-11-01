from infrastructure.page_objects import general
from infrastructure.utilities import base, extensions


def get_record_found_value():
    full_line = extensions.get_text(general.records_found)
    split_line = full_line.split('(')
    split_partial_line = split_line[1].split(')')
    value = split_partial_line[0]
    return value
