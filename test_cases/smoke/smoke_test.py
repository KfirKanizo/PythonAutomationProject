import pytest
from configuration import config
from infrastructure.page_objects import side_bar, general
from infrastructure.utilities import base, extensions, verifications
from infrastructure.work_flows import login_page, pim_page


@pytest.fixture(scope='module')
def session():
    yield base.start_session()
    base.close_session()


def test_admin_login(session):
    login_page.login(config.admin_user, config.admin_pass)
    username = extensions.get_text(general.txt_username)
    verifications.equals(username, "Paul Collings")


def test_add_employee(session):
    login_page.login(config.admin_user, config.admin_pass)
    before_record = int(pim_page.get_record_found_value())
    pim_page.create_employee("Kfir", "Kanizo", "7777")
    extensions.click(side_bar.btn_pim)
    after_record = int(pim_page.get_record_found_value())
    verifications.equals_plus(after_record, before_record, 1)
