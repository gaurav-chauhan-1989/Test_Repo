from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome(executable_path='E:\Selenium\chromedriver.exe')
e1 = driver.find_element(By.XPATH, "//div[@id, 'locator1']")
e2 = driver.find_element(By.XPATH, "//div[@id, 'locator2']")
wait = WebDriverWait(driver, 10)
wait.until(ec.element_to_be_clickable((By.XPATH, "//locator2")))
actions = ActionChains(driver)
actions.move_to_element(e1).click().perform()
actions.context_click(e1).perform()
actions.drag_and_drop(e1, e2).perform()
driver.get_screenshot_as_file("filename")
driver.execute_script("window.scrollBy(0,500)", "")
driver.execute_script("window.scrollBy (0,documents.body.scrollHeight)")
driver.execute_script("arguments[0].scrollIntoView();", e1)
select = Select(e2)
select.select_by_visible_text("sept")
a = select.options
for i in a:
    print(i.text)
driver.switch_to.frame(e2)
driver.switch_to.default_content()
alert = driver.switch_to.alert
alert.accept()
alert.dismiss()
print(alert.text)
parent = driver.current_window_handle
handles = driver.window_handles
for screen in handles:
    driver.switch_to.window(screen)
    if screen!=parent:
        driver.find_element(By.XPATH,"Locator3").send_keys("Hello")

    driver.switch_to.window(parent)






