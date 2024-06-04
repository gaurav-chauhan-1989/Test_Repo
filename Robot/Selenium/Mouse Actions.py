from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome('E:\Selenium\chromedriver.exe')
driver.maximize_window()
driver.get('https://testautomationpractice.blogspot.com/')
wait=WebDriverWait(driver,10, poll_frequency=2)
wait.until(ec.element_to_be_clickable((By.XPATH,"//button[@ondblclick='myFunction1()']")))
e1=driver.find_element(By.XPATH,"//button[@ondblclick='myFunction1()']")
actions=ActionChains(driver)
actions.double_click(e1).perform()
source=driver.find_element(By.ID,"draggable")
destination=driver.find_element(By.ID,"droppable")
driver.execute_script("arguments[0].scrollIntoView();",source)
actions.drag_and_drop(source,destination).perform()
e1 = driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
driver.execute_script("arguments[0].scrollIntoView();", e1)
actions.drag_and_drop_by_offset(e1, 42, 0).perform()
actions.key_down(Keys.CONTROL).send_keys('F').key_up(Keys.CONTROL).perform()
sleep(5)
driver.close()

