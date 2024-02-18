# import logging

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Edge
from selenium.webdriver import Firefox
from utilities.readProperties import ReadConfig
from utilities.custom_Logger import Log_Generator
logger = Log_Generator.log_gen()


@pytest.fixture()
def setup_and_teardown(request):
    # browser_list = ['chrome', 'firefox', 'edge']
    if browser == 'chrome':
        driver = Chrome()
        logger.info("-----Chrome browser launched----")
    elif browser == 'firefox':
        driver = Firefox()
        logger.info("-----Firefox browser launched----")
    elif browser == ' edge':
        driver = Edge()
        logger.info("-----Edge browser launched----")
    else:
        driver = Chrome()
        logger.info("-----Chrome browser launched----")
    driver.get(ReadConfig.get_base_url())
    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver
    driver.close()
    driver.quit()


def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')
