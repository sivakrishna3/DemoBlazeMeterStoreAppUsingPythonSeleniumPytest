import time
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.About_Us_Page import About_us_Page
from utilities.custom_Logger import Log_Generator

# import logging


class TestCase004AboutUsPage:

    About_us_open_message = "//*[@id='videoModalLabel']"
    VIDEO_CLOSE_BUTTON = "//*[@id='videoModal']/div/div/div[3]/button"

    logger = Log_Generator.log_gen()

    # def test_case_001_validate_about_us_button(self, setup_and_teardown):
    #     self.logger.info("-------------test_case_001_validate_about_us_button--------------")
    #     self.logger.info("----------------Validating About Us Page----------------")
    #     self.driver = setup_and_teardown
    #     self.abt_page = About_us_Page(self.driver)
    #     self.abt_page.click_on_about_us_button()
    #     message = self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_BUTTON)
    #     act_message = message.text
    #     if act_message == "Close":
    #         self.logger.info("---------------Test case 001 is Passed------------------")
    #         assert True
    #     else:
    #         time.sleep(5)
    #         self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_001.png")
    #         self.logger.error("-------------Test case 001 is Failed--------------")
    #         assert False

    def test_case_002_validate_clicking_on_video_button(self, setup_and_teardown):
        self.logger.info("-------------test_case_002_validate_clicking_on_video_button--------------")
        self.logger.info("----------------Validating clicking on video button----------------")
        self.driver = setup_and_teardown
        self.abt_page = About_us_Page(self.driver)
        self.abt_page.click_on_video_button()
        message = self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_BUTTON)
        act_message = message.text
        print(act_message)
        if act_message == "Close":
            self.logger.info("---------------Test case 002 is Passed------------------")
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_002.png")
            self.logger.error("-------------Test case 002 is Failed--------------")
            assert False

    # def test_case_003_validate_video_pause_button(self, setup_and_teardown):
    #     self.logger.info("-------------test_case_003_validate_video_pause_button--------------")
    #     self.logger.info("----------------Validating video pause button----------------")
    #     self.driver = setup_and_teardown
    #     self.abt_page = About_us_Page(self.driver)
    #     self.abt_page.click_on_video_pause_button()
    #     message = self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_BUTTON)
    #     act_message = message.text
    #     if act_message == "Close":
    #         self.logger.info("---------------Test case 003 is Passed------------------")
    #         assert True
    #     else:
    #         time.sleep(5)
    #         self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_003.png")
    #         self.logger.error("-------------Test case 003 is Failed--------------")
    #         assert False

