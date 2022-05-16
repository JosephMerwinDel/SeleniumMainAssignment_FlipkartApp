import time

from PageObjects.BaseClass import BaseClassPage
from PageObjects.FashionPage import FashionPage
from PageObjects.GroceryPage import GroceryPage
from PageObjects.ManageAddressPage import ManageAddressPage
from Utils.locators import HomePageLocators


class HomePage(BaseClassPage):

    def __init__(self, driver):
        self.locator = HomePageLocators
        super().__init__(driver)

    def get_homepage_title(self):
        return self.get_title()

    def add_items_to_cart(self):
        grocery_page = GroceryPage(self.driver)
        self.select_grocery(grocery_page)
        self.select_personal_baby_care(grocery_page)
        self.select_home_kitchen(grocery_page)

    def select_grocery(self, grocery_page):
        self.find_element(*self.locator.grocery).click()
        self.hover(*self.locator.hover_snacks)
        e = self.find_element(*self.locator.select_biscuits)
        e.click()
        time.sleep(2)
        grocery_page.select_items()

    def select_personal_baby_care(self, grocery_page):
        self.hover(*self.locator.hover_personal_baby_care)
        e = self.find_element(*self.locator.select_perfume)
        e.click()
        time.sleep(2)
        grocery_page.select_items()

    def select_home_kitchen(self, grocery_page):
        self.hover(*self.locator.hover_Home_Kitchen)
        e = self.find_element(*self.locator.select_cookware)
        e.click()
        time.sleep(2)
        grocery_page.select_items()

    def select_fashion(self):
        fashion_page = FashionPage(self.driver)
        self.hover(*self.locator.hover_fashion)
        e = self.find_element(*self.locator.select_menswear)
        e.click()
        time.sleep(2)
        fashion_page.select_fashion_items()

    def select_my_profile(self, userdata):
        manage_address = ManageAddressPage(self.driver)
        self.hover(*self.locator.hover_over_my_account)
        ele = self.find_element(*self.locator.select_my_profile)
        self.driver.execute_script("arguments[0].click();", ele)
        saved_data = manage_address.add_new_address(userdata)
        return saved_data
