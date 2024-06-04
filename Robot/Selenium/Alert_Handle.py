import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
al = driver.find_element(By.XPATH, "//button[text()='Prompt']")
al.click()
time.sleep(2)
alert = Alert(driver)
print(alert.text)
alert.dismiss()
time.sleep(2)
driver.close()