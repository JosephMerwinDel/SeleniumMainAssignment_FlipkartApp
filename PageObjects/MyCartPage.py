import random
import time

from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException

from PageObjects.BaseClass import BaseClassPage
from Utils.locators import GroceryPageLocators, MyCartPageLocators


class MyCartPage(BaseClassPage):

    def __init__(self, driver):
        self.locator = MyCartPageLocators
        super().__init__(driver)

    def cart_details(self):
        cart_list = []
        self.find_element(*self.locator.cart).click()
        self.find_element(*self.locator.view_all_items).click()

        elements = self.find_elements_by_xpath(*self.locator.get_item_names_from_cart)
        for item in elements:
            cart_list.append(item.text.strip())

        return cart_list

    def remove_cart(self):
        self.find_element(*self.locator.close_view_cart).click()
        time.sleep(1)
        self.find_element(*self.locator.remove_from_cart).click()
        time.sleep(1)
        self.find_element(*self.locator.confirm_remove).click()
        time.sleep(2)
