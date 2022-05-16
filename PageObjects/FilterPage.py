import random
import time

from selenium.webdriver import Keys

from PageObjects.BaseClass import BaseClassPage
from Utils.locators import SearchAndFilterPage


class FilterPage(BaseClassPage):

    def __init__(self, driver):
        self.locator = SearchAndFilterPage
        super().__init__(driver)

    def search_and_filter(self, filter_item="Besan"):
        search_filter_list =[]
        self.find_element(*self.locator.search).send_keys(filter_item)
        self.find_element(*self.locator.search).send_keys(Keys.SPACE)
        time.sleep(2)
        elements = self.find_elements_by_xpath(*self.locator.searchlist_items)
        try:
            ele = random.choice(elements)
            print(ele.text)
            self.driver.execute_script("arguments[0].click();", ele)
        except Exception:
            print("No items found")
        time.sleep(3)
        elements = self.find_elements_by_xpath(*self.locator.get_items_from_search)
        for item in elements:
            search_filter_list.append(item.text)
        return search_filter_list
