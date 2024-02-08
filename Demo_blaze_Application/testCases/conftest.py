import logging

import pytest
from selenium.webdriver import Chrome
from utilities.readProperties import ReadConfig


@pytest.fixture()
def setup_and_teardown():
    driver = Chrome()
    driver.get(ReadConfig.get_base_url())
    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver
    driver.close()
    driver.quit()



