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

    About_us_open_message = "//*[@id='logInModalLabel']"
    VIDEO_CLOSE_BUTTON = "//*[@id='videoModal']/div/div/div[3]/button"

    logger = Log_Generator.log_gen()

    def test_case_001_validate_about_us_button(self, setup_and_teardown):
        self.logger.info("-------------test_case_001_validate_about_us_button--------------")
        self.logger.info("----------------Validating About Us Page----------------")
        self.driver = setup_and_teardown
        self.abt_page = About_us_Page(self.driver)
        self.abt_page.click_on_about_us_button()
        message = self.driver.find_element(By.XPATH, self.About_us_open_message)
        act_message = message.text
        try:
            if act_message == "About us":
                self.logger.info("---------------Test case 001 is Passed------------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_001.png")
                self.logger.error("-------------Test case 001 is Failed--------------")
                assert False
        except Exception as e:
            print(e)
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_001.png")
            self.logger.error("-------------Test case 001 is Failed--------------")
            assert False

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

    def test_case_003_validate_mute_video(self, setup_and_teardown):
        self.logger.info("-------------test_case_003_validate_mute_video--------------")
        self.logger.info("----------------Validating Muting the Video----------------")
        self.driver = setup_and_teardown
        self.abt_page = About_us_Page(self.driver)
        self.abt_page.click_on_volume_mute_button()
        # Perform assertion to check if the video is muted
        # Example assertion code: assert self.abt_page.is_video_muted(), "Test case 003 Failed"

    def test_case_004_validate_pause_video(self, setup_and_teardown):
        self.logger.info("-------------test_case_004_validate_pause_video--------------")
        self.logger.info("----------------Validating Pausing the Video----------------")
        self.driver = setup_and_teardown
        self.abt_page = About_us_Page(self.driver)
        self.abt_page.click_on_video_pause_button()
        # Perform assertion to check if the video is paused
        # Example assertion code: assert self.abt_page.is_video_paused(), "Test case 004 Failed"

    def test_case_005_validate_maximize_video(self, setup_and_teardown):
        self.logger.info("-------------test_case_005_validate_maximize_video--------------")
        self.logger.info("----------------Validating Maximizing the Video----------------")
        self.driver = setup_and_teardown
        self.abt_page = About_us_Page(self.driver)
        self.abt_page.click_on_full_screen_button()
        # Perform assertion to check if the video is maximized
        # Example assertion code: assert self.abt_page.is_video_maximized(), "Test case 005 Failed"

    def test_case_006_validate_mouse_actions_on_video(self, setup_and_teardown):
        self.logger.info("-------------test_case_006_validate_mouse_actions_on_video--------------")
        self.logger.info("----------------Validating Mouse Actions on Video----------------")
        self.driver = setup_and_teardown
        self.abt_page = About_us_Page(self.driver)
        # Perform mouse actions on the video, e.g., move, click, etc.
        # Example assertion code: assert self.abt_page.perform_mouse_actions(), "Test case 006 Failed"

    def test_case_007_validate_volume_increase(self, setup_and_teardown):
        self.logger.info("-------------test_case_007_validate_volume_increase--------------")
        self.logger.info("----------------Validating Volume Increase----------------")
        self.driver = setup_and_teardown
        self.abt_page = About_us_Page(self.driver)
        self.abt_page.click_on_volume_button()
        # Perform assertion to check if the volume is increased
        # Example assertion code: assert self.abt_page.is_volume_increased(), "Test case 007 Failed"

    def test_case_008_validate_close_video(self, setup_and_teardown):
        self.logger.info("-------------test_case_009_validate_close_video--------------")
        self.logger.info("----------------Validating Closing the Video----------------")
        self.driver = setup_and_teardown
        self.abt_page = About_us_Page(self.driver)
        self.abt_page.click_on_video_close_button()
        # Perform assertion to check if the video is closed
        # Example assertion code: assert self.abt_page.is_video_closed(), "Test case 009 Failed"

