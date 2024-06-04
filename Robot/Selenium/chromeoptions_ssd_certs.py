from selenium import webdriver

options=webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(executable_path="E:\Selenium\geckodriver.exe", chrome_options=options)