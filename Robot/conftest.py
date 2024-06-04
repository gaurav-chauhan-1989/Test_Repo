import inspect

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import logging

def pytest_addoption(parser):
    parser.addoption("--browser")

'''@pytest.hookimpl
def pytest_sessionstart(session):
    print("Hello from pytest_sessionstart hook!")

@pytest.hookimpl
def pytest_sessionfinish(session):
    print("Hello from pytest_sessionfinish hook!")'''

'''@pytest.hookimpl
def pytest_runtest_setup(item):
    print("Hook before test start")

@pytest.hookimpl
def pytest_runtest_teardown(item):
    print("Hook after test end")'''

@pytest.fixture(scope='class')
def init_driver(request):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    browser = request.config.getoption("--browser")
    if browser == 'Chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == 'Firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == 'Edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture
def custom_logger(level=logging.DEBUG):
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    fh = logging.FileHandler("test_log.logs")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
