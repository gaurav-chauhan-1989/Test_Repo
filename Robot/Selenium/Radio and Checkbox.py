from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome("E:\Selenium\chromedriver.exe")
driver.maximize_window()
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html')
driver.implicitly_wait(10)

try:
    e1=driver.find_element(By.ID,"RESULT_RadioButton-7_1").is_selected()
    print(e1)
    driver.find_element(By.XPATH,"//label[@for='RESULT_RadioButton-7_1']").click()
    e1=driver.find_element(By.ID,"RESULT_RadioButton-7_1").is_selected()
    print(e1)
    driver.find_element(By.XPATH,"//label[@for='RESULT_CheckBox-8_0']").click()
    e2=driver.find_element(By.ID,"RESULT_CheckBox-8_0").is_selected()
    print(e2)

finally:
    driver.close()
