
import time

import pytest
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
from Config.TestData import Test_Data
from Pages.BasePage import Base_Page

class login_page(Base_Page):

    name = (By.ID, "name")
    email = (By.ID, "email")
    phone = (By.ID, "phone")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Test_Data.url)
        self.driver.maximize_window()

    def login_meth(self, name, email, phone):

        self.set_text(self.name, name)
        time.sleep(5)
        self.set_text(self.email, email)
        time.sleep(5)
        self.set_text(self.phone, phone)
        time.sleep(5)
