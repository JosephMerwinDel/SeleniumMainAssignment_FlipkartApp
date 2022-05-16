import time
import random

from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException
from selenium.webdriver.support.select import Select

from PageObjects.BaseClass import BaseClassPage
from Utils.Read_xlsx import XlsxReader
from Utils.locators import FashionPageLocators, MyProfileLocators


class ManageAddressPage(BaseClassPage):

    def __init__(self, driver):
        self.locator = MyProfileLocators
        super().__init__(driver)

    def add_new_address(self, user_data):
        saved_data = {}
        self.find_element(*self.locator.manage_address).click()
        self.find_element(*self.locator.add_new_address).click()
        self.find_element(*self.locator.name).send_keys(user_data.get("name", 0))
        self.find_element(*self.locator.phone).send_keys(user_data.get("mobile_no", 0))
        self.find_element(*self.locator.pincode).send_keys(user_data.get("pincode", 0))
        self.find_element(*self.locator.locality).send_keys(user_data.get("locality", 0))
        self.find_element(*self.locator.address).send_keys(user_data.get("address", 0))
        if user_data.get("address_type") == 'Home':
            self.find_element(*self.locator.address_type_home).click()
        elif user_data.get("address_type") == 'Work':
            self.find_element(*self.locator.address_type_work).click()
        self.find_element(*self.locator.save).click()
        time.sleep(2)
        saved_data["name"] = self.find_element(*self.locator.get_saved_name).text
        saved_data["mobile_no"] = self.find_element(*self.locator.get_saved_number).text
        saved_data["address"] = self.find_element(*self.locator.get_address).text
        return saved_data

