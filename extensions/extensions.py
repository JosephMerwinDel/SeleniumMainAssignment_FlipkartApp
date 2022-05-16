from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium import webdriver


class WebDriverExtended(webdriver):
    def __init__(self, driver, config):
        super().__init__(driver)
        self.base_url = config["base_url"]

    def open(self):
        self.get(self.base_url)
