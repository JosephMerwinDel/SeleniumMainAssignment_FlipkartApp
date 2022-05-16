import time
import random

from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException

from PageObjects.BaseClass import BaseClassPage
from Utils.locators import GroceryPageLocators


class GroceryPage(BaseClassPage):
    list_of_items_added_to_cart = []

    def __init__(self, driver):
        self.locator = GroceryPageLocators
        super().__init__(driver)

    def select_items(self, count_of_items_to_choose=3):
        count = 0
        elements = self.find_elements_by_xpath(*self.locator.get_items_in_grocery)
        while count < count_of_items_to_choose:
            try:
                ele = random.choice(elements[:10])
                item_name = ele.text
                elements.remove(ele)
                loc = self.locator.select_item_1 + ele.text[:30].strip() + self.locator.select_item_2
                ele = self.element_clickable(loc)
                time.sleep(1)
                self.execute_script(ele)
                GroceryPage.list_of_items_added_to_cart.append(item_name.strip())
                count += 1
            except NoSuchElementException:
                print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME!")
                self.driver.quit()
            except InvalidSelectorException:
                print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME!")
                self.driver.quit()



