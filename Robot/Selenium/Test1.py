from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


options = ChromiumOptions
options.headless = True
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(Service= ChromeService(ChromeDriverManager().install()), options=options)
driver.maximize_window()
e1 = driver.find_element(By.ID, "ID1")
WebDriverWait(driver, 10, poll_frequency=1).until(ec.element_to_be_clickable((By.ID, "E1")))
parent = driver.current_window_handle
handles = driver.window_handles

for handle in handles:
    if handle != parent:
        driver.switch_to.window(handle)
        driver.find_element(By.XPATH,"//div[@id='E2']").click()
        driver.close()
driver.switch_to.window(parent)


