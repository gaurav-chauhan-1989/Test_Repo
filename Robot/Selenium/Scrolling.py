from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path='E:\Selenium\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')

driver.execute_script("window.scrollBy(0,500)","")                               # Scroll a/c to pixels
time.sleep(5)
e1=driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
driver.execute_script("arguments[0].scrollIntoView();",e1)                       # Scroll till element is visible
time.sleep(5)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")           # scroll till end of the page