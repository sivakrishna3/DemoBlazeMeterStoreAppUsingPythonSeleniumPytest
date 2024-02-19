import time
import pytest
from selenium.common import TimeoutException
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.About_Us_Page import About_us_Page
from utilities.custom_Logger import Log_Generator

# import logging


class TestCase004AboutUsPage:

    About_us_open_message = "//h5[@id='videoModalLabel']"
    VIDEO_CLOSE_BUTTON = "//*[@id='videoModal']/div/div/div[3]/button"
    VIDEO_CLOSE_X_MARK = "//*[@id='videoModal']/div/div/div[1]/button/span"
    Pause_text = "//*[@id='example-video']/div[4]/button[1]/span[2]"
    unmute_text = "//span[normalize-space()='Unmute']"
    pic_in_pic = "//span[normalize-space()='Exit Picture-in-Picture']"
    full_screen = "//span[normalize-space()='Non-Fullscreen']"
    logger = Log_Generator.log_gen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_case_001_validate_about_us_button(self, setup_and_teardown):
        self.logger.info("-----test_case_001_validate_about_us_button--------------")
        self.logger.info("-----Verifying About Us Page----------------")
        self.driver = setup_and_teardown
        self.abt_page = About_us_Page(self.driver)
        self.abt_page.click_on_about_us_button()
        try:
            is_displayed = self.driver.find_element(By.XPATH, self.About_us_open_message).is_displayed()
            self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_BUTTON).click()
            if is_displayed:
                if is_displayed == "About us":
                    self.logger.info("----- Test case 001 is Passed ------------------")
                    assert True
                else:
                    time.sleep(5)
                    self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_001.png")
                    self.logger.error("----- Test case 001 is Failed --------------")
                    assert False
        except TimeoutException as e:
            print(e)
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_001.png")
            self.logger.error("-----Test case 001 is not executed (Failed)--------------")
            assert False

    @pytest.mark.regression
    def test_case_002_validate_video_close_button(self, setup_and_teardown):
        self.logger.info("-----test_case_002_validate_video_close_button--------------")
        self.logger.info("-----Verifying About Us Page----------------")
        self.driver = setup_and_teardown
        self.abt_page = About_us_Page(self.driver)
        self.abt_page.click_on_video_close_button()
        act_title = self.driver.title
        exp_title = 'STORE'
        try:
            if act_title == exp_title:
                self.logger.info("----- Test case 002 is Passed------------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_002.png")
                self.logger.error("----- Test case 002 is Failed--------------")
                assert False
        except TimeoutException as e:
            print(e)
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_002.png")
            self.logger.error("-----Test case 002 is no executed (Failed)--------------")
            assert False

    @pytest.mark.regression
    def test_case_003_validate_video_close_x_mark(self, setup_and_teardown):
        self.logger.info("-----test_case_003_validate_video_close_x_mark--------------")
        self.logger.info("-----Verifying About Us Page----------------")
        self.driver = setup_and_teardown
        self.abt_page = About_us_Page(self.driver)
        self.abt_page.click_on_video_close_x_mark()
        try:
            is_displayed = self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_X_MARK).is_displayed()
            self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_X_MARK).click()
            message = self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_X_MARK)
            if is_displayed:
                if message.text == 'x':
                    self.logger.info("----- Test case 003 is Passed------------------")
                    assert True
                else:
                    time.sleep(5)
                    self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_003.png")
                    self.logger.error("----- Test case 003 is Failed--------------")
                    assert False
        except TimeoutException as e:
            print(e)
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_003.png")
            self.logger.error("----- Test case 003 is  not executed (Failed)--------------")
            assert False

    @pytest.mark.regression
    def test_case_004_validate_clicking_on_video_button(self, setup_and_teardown):
        self.logger.info("-----test_case_004_validate_clicking_on_video_button--------------")
        self.logger.info("-----Verifying About Us Page----------------")
        self.driver = setup_and_teardown
        self.abt_page = About_us_Page(self.driver)
        self.abt_page.click_on_video_button()
        message = self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_BUTTON)
        act_message = message.text
        print(act_message)
        try:
            if act_message == "Close":
                self.logger.info("----- Test case 004 is Passed------------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_004.png")
                self.logger.error("----- Test case 004 is Failed--------------")
                assert False
        except TimeoutException as e:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_004.png")
            self.logger.error("----- Test case 004 is Failed--------------")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_case_005_validate_video_pause_button(self, setup_and_teardown):
        self.logger.info("-----test_case_005_validate_video_pause_button--------------")
        self.logger.info("-----Verifying About Us Page----------------")
        self.driver = setup_and_teardown
        self.abt_page = About_us_Page(self.driver)
        self.abt_page.click_on_video_pause_button()
        try:
            message = self.driver.find_element(By.XPATH, self.Pause_text).text
            print(message)
            if message == "Play":
                self.logger.info("----- Test case 005 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_005.png")
                self.logger.error("----- Test case 005 is Failed-----")
                assert False
        except TimeoutException as e:
            print(e)
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_005.png")
            self.logger.error("----- Test case 005 is Failed--------------")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_case_006_validate_video_volume_mute_button(self, setup_and_teardown):
        self.logger.info("-----test_case_006_validate_video_volume_mute_button--------------")
        self.logger.info("-----Verifying About Us Page----------------")
        self.driver = setup_and_teardown
        self.abt_page = About_us_Page(self.driver)
        self.abt_page.click_on_volume_mute_button()
        try:
            is_displayed = self.driver.find_element(By.XPATH, self.unmute_text).is_displayed()
            self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_BUTTON).click()
            if is_displayed:
                message = self.driver.find_element(By.XPATH, self.unmute_text).text
                print(message)
                if message == "Unmute":
                    self.logger.info("----- Test case 006 is Passed-----")
                    assert True
                else:
                    time.sleep(5)
                    self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_006.png")
                    self.logger.error("----- Test case 006 is Failed-----")
                    assert False
        except TimeoutException as e:
            print(e)
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_006.png")
            self.logger.error("----- Test case 006 is Failed--------------")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_case_007_validate_video_picture_in_picture_button(self, setup_and_teardown):
        self.logger.info("-----test_case_007_validate_video_picture_in_picture_button--------------")
        self.logger.info("-----Verifying video picture in picture button----------------")
        self.driver = setup_and_teardown
        self.abt_page = About_us_Page(self.driver)
        self.abt_page.click_on_pic_in_pic_button()
        try:
            # is_displayed = self.driver.find_element(By.XPATH, self.pic_in_pic).is_displayed()
            # if is_displayed:
            message = self.driver.find_element(By.XPATH, self.pic_in_pic).text
            print(message)
            if message == "Exit Picture-in-Picture":
                self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_BUTTON).click()
                self.logger.info("----- Test case 007 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_007.png")
                self.logger.error("----- Test case 007 is Failed-----")
                assert False
        except TimeoutException as e:
            print(e)
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_007.png")
            self.logger.error("----- Test case 007 is Failed--------------")
            assert False
    #

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_case_008_validate_video_full_screen_button(self, setup_and_teardown):
        self.logger.info("-----test_case_008_validate_video_full_screen_button--------------")
        self.logger.info("-----Verifying video picture in picture button----------------")
        self.driver = setup_and_teardown
        self.abt_page = About_us_Page(self.driver)
        self.abt_page.click_on_full_screen_button()
        try:
            is_displayed = self.driver.find_element(By.XPATH, self.full_screen).is_displayed()
            message = self.driver.find_element(By.XPATH, self.full_screen).text
            print(message)
            if is_displayed:
                if message == "Non-Fullscreen":
                    self.logger.info("----- Test case 008 is Passed-----")
                    assert True
                else:
                    time.sleep(5)
                    self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_008.png")
                    self.logger.error("----- Test case 008 is Failed-----")
                    assert False
        except TimeoutException as e:
            print(e)
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_008.png")
            self.logger.error("----- Test case 008 is Failed--------------")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_case_009_validate_video_volume_handling_button(self, setup_and_teardown):
        self.logger.info("-----test_case_009_validate_video_volume_handling_button--------------")
        self.logger.info("-----Verifying video picture in picture button----------------")
        self.driver = setup_and_teardown
        self.abt_page = About_us_Page(self.driver)
        self.abt_page.click_on_video_volume_handle_button("-40")
        try:
            if self.driver.title == "STORE":
                self.logger.info("----- Test case 009 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_009.png")
                self.logger.error("----- Test case 009 is Failed-----")
                assert False
        except TimeoutException as e:
            print(e)
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\About_Us_Page\\" + "test_case_009.png")
            self.logger.error("----- Test case 009 is Failed--------------")
            assert False
