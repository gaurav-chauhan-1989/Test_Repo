from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Base_Page():
    def __init__(self, driver):
        self.driver = driver

    def element_click(self, locator):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator)).click()

    def set_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).send_keys(text)

