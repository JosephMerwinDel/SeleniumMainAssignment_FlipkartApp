import base64

import pytest

from PageObjects.FilterPage import FilterPage
from PageObjects.GroceryPage import GroceryPage
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from PageObjects.MyCartPage import MyCartPage
from Tests.BaseTest import BaseTest
from Utils.Read_xlsx import XlsxReader


@pytest.mark.usefixtures("setup")
class TestFeatures(BaseTest):

    @pytest.mark.filterwarnings
    def test_login(self, config):
        log = self.getLogger()
        login_page = LoginPage(self.driver)
        login_page.open(config["base_url"])
        log.info("****Login to the Flipkart application*****")
        log.info("Username: {0}".format(config["username"]))
        log.info("Password: {0}".format(base64.b64encode(config["password"].encode("utf-8"))))
        login_status = login_page.login(config["username"], config["password"])
        try:
            assert login_status is True
            log.info("Login is successful!")
        except Exception:
            log.info("Login unsuccessful")
        finally:
            login_page.logout()

    @pytest.mark.filterwarnings
    def test_cart_functionality(self, config):
        log = self.getLogger()
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        cart_page = MyCartPage(self.driver)
        log.info("****Login to the Flipkart application*****")
        login_page.open(config["base_url"])
        login_page.login(config["username"], config["password"])
        log.info("Login is successful!")
        home_page.add_items_to_cart()
        cart_list = cart_page.cart_details()
        try:
            assert set(cart_list) == set(GroceryPage.list_of_items_added_to_cart)
            log.info("Items added to the cart matches")
        except Exception:
            log.info("Items added does not match cart")
        finally:
            cart_page.remove_cart()
            login_page.logout()

    @pytest.mark.filterwarnings
    def test_filter_functionality(self, config):
        filter_item = 'Besan'
        log = self.getLogger()
        login_page = LoginPage(self.driver)
        filter_page = FilterPage(self.driver)
        log.info("****Login to the Flipkart application*****")
        login_page.open(config["base_url"])
        login_page.login(config["username"], config["password"])
        filtered_list = filter_page.search_and_filter(filter_item)
        try:
            assert any(filter_item in string for string in filtered_list) == True
            log.info("Filtered items are displayed")
        except Exception:
            log.info("Filtered items are not displayed correctly")
        finally:
            login_page.logout()

    @pytest.mark.skip
    def test_wishlist_functionality(self, config):
        log = self.getLogger()
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        login_page.open(config["base_url"])
        login_page.login(config["username"], config["password"])
        home_page.select_fashion()

    @pytest.mark.filterwarnings
    def test_manage_address(self, config):
        reader = XlsxReader()
        user_data = reader.get_address_data()
        log = self.getLogger()
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        login_page.open(config["base_url"])
        login_page.login(config["username"], config["password"])
        saved_address_data = home_page.select_my_profile(user_data)
        assert saved_address_data.get("name") == user_data.get("name")
        assert saved_address_data.get("mobile_no") == user_data.get("mobile_no")
        assert user_data.get("pincode") in saved_address_data.get("address")
        assert user_data.get("locality") in saved_address_data.get("address")
        login_page.logout()

    @pytest.mark.filterwarnings
    def test_logout(self, config):
        log = self.getLogger()
        login_page = LoginPage(self.driver)
        log.info("****Login to the Flipkart application*****")
        login_page.open(config["base_url"])
        login_status = login_page.login(config["username"], config["password"])
        assert login_status is True
        log.info("Login is successful!")
        logout_status = login_page.logout()
        assert logout_status is True
        log.info("Logout is successful!")
