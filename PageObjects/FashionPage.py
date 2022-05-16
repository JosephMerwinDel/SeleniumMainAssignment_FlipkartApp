import time
import random

from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException

from PageObjects.BaseClass import BaseClassPage
from Utils.locators import FashionPageLocators


class FashionPage(BaseClassPage):

    def __init__(self, driver):
        self.locator = FashionPageLocators
        super().__init__(driver)

    def select_fashion_items(self, count_of_items_to_choose=2):
        count = 0
        print("before")
        elements = self.find_elements_by_xpath(*self.locator.select_items_from_list)
        time.sleep(2)
        while count < count_of_items_to_choose:
            try:
                ele = random.choice(elements[:10])
                item_name = ele.text
                print(item_name)
                elements.remove(ele)
                loc = self.locator.click_wishlist_1 + ele.text.strip() + self.locator.click_wishlist_2

                ele = self.element_clickable("//*[local-name()='svg']/*[localname()='path']")
                self.hover_by_xpath(ele)
                time.sleep(1)
                self.execute_script(ele)
                #GroceryPage.list_of_items_added_to_cart.append(item_name.strip())
                #self.log.info("The Following item is added to the cart: {0}".format(item_name.strip()))
                count += 1
            except NoSuchElementException:
                print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME!")
                self.driver.quit()
            except InvalidSelectorException:
                print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME!")
                self.driver.quit()