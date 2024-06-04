from selenium import webdriver

driver=webdriver.Chrome(executable_path='E:\Selenium\chromedriver.exe')
driver.get('http://www.facebook.com')
driver.maximize_window()
driver.get_screenshot_as_file("E:\Selenium\Pics\home.jpg")                # Take screenshot and save in the given location