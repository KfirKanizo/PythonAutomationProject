import pytest
from configuration import config
from infrastructure.utilities import base, extensions
from infrastructure.work_flows import login_page, pim_page


@pytest.fixture(scope='module')
def session():
    yield base.start_session()
    base.close_session()


def test_admin_login(session):
    login_page.login(config.admin_user, config.admin_pass)


def test_add_employee(session):
    first_record = pim_page.get_record_found_value()



