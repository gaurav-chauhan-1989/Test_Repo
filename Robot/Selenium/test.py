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
rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
cols = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/th"))
a = []
for i in range(2, rows+1):
    for j in range(1, cols+1):
        a.append(driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{i}]/td[{j}]").text)

print(a)


