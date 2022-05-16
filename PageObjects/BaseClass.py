
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClassPage(object):
    def __init__(self, driver, base_url='https://www.flipkart.com/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        try:
            elem = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print
            "Loading took too much time!"
        return elem

    def find_element_by_xpath(self, value):
        return self.driver.find_element(By.XPATH, value= value)

    def is_displayed(self, *locator):
        element = self.find_element(*locator)
        return element.is_displayed()

    def find_elements_by_xpath(self, *locator):
        return self.driver.find_elements(*locator)

    def open(self, url):
        self.driver.get(url)

    def execute_script(self, element):
        self.driver.implicitly_wait(self.timeout)
        self.driver.execute_script("arguments[0].click();", element)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def hover_by_xpath(self, element):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_element(self, *locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()
        except StaleElementReferenceException as e:
            print(e)

    def element_clickable(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((By.XPATH, locator)))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()

    def presen(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((By.XPATH, locator)))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()

    def stale_exception_check(self, *locator):
        ele = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
        print("Before check")
        print(WebDriverWait(self.driver, self.timeout).until(EC.staleness_of(ele)))


