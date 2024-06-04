from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains                               # Need to import ActionChains to perform mouse actions
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time

driver=webdriver.Chrome(executable_path="E:\Selenium\chromedriver.exe")
driver.get('http://demo.automationtesting.in/Alerts.html')
driver.maximize_window()

driver.implicitly_wait(10)                                              # By default in seconds

e1=driver.find_element(By.XPATH,"//a[@href='SwitchTo.html']")
e2=driver.find_element(By.XPATH,"//a[@href='Windows.html']")
actions=ActionChains(driver)
actions.move_to_element(e1).move_to_element(e2).click().perform()                # Hover on first element then hover on 2nd element
                                                                                 # Click on 2nd element
wait = WebDriverWait(driver,10)
wait.until(ec.element_to_be_clickable((By.XPATH,"//a[@href='#Seperate']")))
driver.find_element(By.XPATH,"//a[@href='#Seperate']").click()
driver.find_element(By.XPATH,"//*[@class='btn btn-primary']").click()
parent=driver.current_window_handle                                              # Will get current window handles
print(parent)
handles = driver.window_handles                                                    # Will get all window handles in browser

for i in handles:
    if i != parent:
        driver.switch_to.window(i)
        print(driver.current_url)
        driver.maximize_window()
        driver.find_element(By.NAME,"mobile1").click()
        driver.close()

driver.switch_to.window(parent)
driver.close()

