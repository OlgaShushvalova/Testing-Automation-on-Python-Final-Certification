from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

ids = dict()
with open("./locators.yaml") as f:
    locators = yaml.safe_load(f)
for locator in locators["xpath"].keys():
    ids[locator] = (By.XPATH, locators["xpath"][locator])
for locator in locators["css"].keys():
    ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while opertion with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

# ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(ids["LOCATOR_PASS_FIELD"], word, description="password form")

# CLICK
    def click_login_button(self):
        self.click_button(ids["LOCATOR_LOGIN_BTN"], description="login")

    def click_about_button(self):
        self.click_button(ids["LOCATOR_ABOUT"], description=" post")

# GET TEXT
    def login_success(self):
        return self.get_text_from_element(ids["LOCATOR_SUCCESS"], description="username")

    def check_about_title(self):
        return self.get_element_property(ids["LOCATOR_TITLE"], property="font-size")


