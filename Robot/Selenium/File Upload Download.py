from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path='E:\Selenium\chromedriver.exe')
driver.get('http://demo.automationtesting.in/Alerts.html')
driver.maximize_window()
e1=driver.find_element(By.XPATH,"//a[@href='#']")
e2=driver.find_element(By.XPATH,"//a[@href='FileUpload.html']")
action=ActionChains(driver)
action.move_to_element(e1).move_to_element(e2).click().perform()
driver.find_element(By.ID,"input-4").send_keys('E:/Selenium/Pics/desktop.jpg')