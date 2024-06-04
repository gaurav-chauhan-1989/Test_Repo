from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
#options.page_load_strategy = 'eager'
option.headless = True
driver = webdriver.Chrome('E:\Selenium\chromedriver.exe')
driver.get('http://demo.guru99.com/test/newtours/')
driver.maximize_window()
driver.find_element(By.XPATH, "//a[@href = 'http://demo.guru99.com/insurance/v1/index.php']").click()
sleep(5)
driver.back()
sleep(5)
driver.forward()
sleep(5)
driver.refresh()
driver.close()