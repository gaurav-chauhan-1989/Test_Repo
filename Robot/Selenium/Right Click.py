from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path='E:\Selenium\chromedriver.exe')
driver.maximize_window()
driver.get('http://swisnl.github.io/jQuery-contextMenu/demo.html')
driver.implicitly_wait(5)
element=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
action=ActionChains(driver)
action.context_click(element).perform()
element2=driver.find_element(By.XPATH,"//li[@class='context-menu-item context-menu-icon context-menu-icon-delete']")
action.move_to_element(element2).click().perform()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
