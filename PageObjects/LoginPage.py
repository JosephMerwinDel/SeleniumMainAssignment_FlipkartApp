import time

from selenium.common.exceptions import StaleElementReferenceException
from PageObjects.BaseClass import BaseClassPage
from Utils.locators import *


class LoginPage(BaseClassPage):

    def __init__(self, driver):
        self.locator = LoginPageLocators
        super().__init__(driver)

    def login(self, username, password):
        self.driver.set_page_load_timeout(10)
        self.find_element(*self.locator.username).send_keys(username)
        self.find_element(*self.locator.password).send_keys(password)
        self.wait_element(*self.locator.login).click()
        time.sleep(2)
        login_success = self.is_displayed(*self.locator.login_success)
        return login_success

    def logout(self):
        self.hover(*self.locator.hover_over_my_account)
        ele = self.wait_element(*self.locator.logout)
        try:
            ele.click()
            time.sleep(3)
            logout_status = self.is_displayed(*self.locator.logout_status)
            return logout_status
        except StaleElementReferenceException as e:
            print(e)
