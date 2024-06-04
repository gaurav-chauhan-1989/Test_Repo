from selenium import webdriver

profile=webdriver.FirefoxProfile()
profile.accept_untrusted_certs=True
driver=webdriver.Firefox(executable_path='E:\Selenium\geckodriver.exe', firefox_profile=profile)
