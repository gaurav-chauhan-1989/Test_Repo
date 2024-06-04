from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path='E:\Selenium\chromedriver.exe')
driver.get('http://www.facebook.com')
driver.maximize_window()
e1=driver.find_element(By.NAME,"birthday_month")
select=Select(e1)
select.select_by_visible_text('Sept')
print(len(select.options))
list = select.options
for i in list:
    print(i.text)