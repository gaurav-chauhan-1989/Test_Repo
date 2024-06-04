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
al = driver.find_element(By.ID, "frame-one796456169")
driver.execute_script("arguments[0].scrollIntoView();", al)
driver.switch_to.frame("frame-one796456169")
driver.find_element(By.ID,"RESULT_TextField-0").send_keys("Gaurav")
time.sleep(2)
driver.switch_to.default_content()
driver.find_element(By.ID, "name").send_keys("Gaurav")
time.sleep(2)
driver.close()