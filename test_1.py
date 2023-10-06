import yaml
from testpage import OperationsHelper
import logging


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_login(browser):
    logging.info("Test login Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    assert testpage.login_success() == f"Hello, {testdata['login']}", "test_login FAILED"


def test_about_font(browser):
    logging.info("Test about_font Starting")
    testpage = OperationsHelper(browser)
    # testpage.go_to_site()
    # testpage.enter_login(testdata["login"])
    # testpage.enter_pass(testdata["password"])
    # testpage.click_login_button()
    testpage.click_about_button()
    assert testpage.check_about_title() == f"{testdata['font']}", "test about_font FAILED"


