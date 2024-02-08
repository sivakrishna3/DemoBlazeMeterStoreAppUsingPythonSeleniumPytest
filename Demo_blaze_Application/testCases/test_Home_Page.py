import pytest
from selenium.webdriver import Chrome
from pageObjects.Home_Page import Home_page
from utilities.readProperties import ReadConfig


class TestCase002HomePage:

    def test_case_001_validate_homepage_button(self, setup_and_teardown):
        self.driver = setup_and_teardown
        self.hm_page = Home_page(self.driver)
        self.hm_page.home_page_button()
        actual_title = self.driver.title
        print(actual_title)
        if actual_title == 'STORE':
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_case_001_homepage_button.png")
            assert False
