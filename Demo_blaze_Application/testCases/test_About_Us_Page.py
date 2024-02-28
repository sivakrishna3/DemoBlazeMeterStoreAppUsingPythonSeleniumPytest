import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common import TimeoutException
# from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from pageObjects.About_Us_Page import About_us_Page
from utilities.readProperties import ReadConfig
from utilities.custom_Logger import Log_Generator


# import logging


@allure.description("validate_about_us_page")
@allure.severity(allure.severity_level.CRITICAL)
class TestCase004AboutUsPage:

    data = ReadConfig.get_json_data()
    try:
        About_us_open_message = data['About_Us_Page']["About_us_open_message"]
        VIDEO_CLOSE_BUTTON = data['About_Us_Page']["VIDEO_CLOSE_BUTTON"]
        VIDEO_CLOSE_X_MARK = data['About_Us_Page']["VIDEO_CLOSE_X_MARK"]
        Pause_text = data['About_Us_Page']["Pause_text"]
        unmute_text = data['About_Us_Page']["unmute_text"]
        pic_in_pic = data['About_Us_Page']["pic_in_pic"]
        non_full_screen = data['About_Us_Page']["non_full_screen"]
    except Exception as e:
        print(f"{e}: No such element found in json file.")

    logger = Log_Generator.log_gen()

    @allure.description("validate_about_us_button")
    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
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
                    self.logger.info("-----Test case 001 is Passed ------------------")
                    assert True
                else:
                    time.sleep(5)
                    self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_001_about_us_page.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_case_001_about_us_page",
                                  attachment_type=AttachmentType.PNG)
                    self.logger.error("-----Test case 001 is Failed --------------")
                    assert False
        except TimeoutException as e:
            print(e)
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_001_about_us_page.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_case_001_about_us_page",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("-----Test case 001 is not executed (Failed)--------------")
            assert False

    @pytest.mark.regression
    @allure.severity(allure.severity_level.MINOR)
    def test_case_002_validate_video_close_button(self, setup_and_teardown):
        self.logger.info("-----test_case_002_validate_video_close_button--------------")
        self.logger.info("-----Verifying video_close_button----------------")
        self.driver = setup_and_teardown
        self.abt_page = About_us_Page(self.driver)
        self.abt_page.click_on_video_close_button()
        try:
            is_displayed = self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_BUTTON).is_displayed()
            if is_displayed:
                message = self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_BUTTON).text
                self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_BUTTON).click()
                if message == "Close":
                    self.logger.info("----- Test case 002 is Passed------------------")
                    assert True
                else:
                    time.sleep(5)
                    self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_002_about_us_page.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_case_002_about_us_page",
                                  attachment_type=AttachmentType.PNG)
                    self.logger.error("----- Test case 002 is Failed--------------")
                    assert False
        except TimeoutException as e:
            print(e)
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_002_about_us_page.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_case_002_about_us_page",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("-----Test case 002 is no executed (Failed)--------------")
            assert False

    @pytest.mark.regression
    @allure.severity(allure.severity_level.MINOR)
    def test_case_003_validate_video_close_x_mark(self, setup_and_teardown):
        self.logger.info("-----test_case_003_validate_video_close_x_mark--------------")
        self.logger.info("-----Verifying validate_video_close_x_mark----------------")
        self.driver = setup_and_teardown
        self.abt_page = About_us_Page(self.driver)
        self.abt_page.click_on_video_close_x_mark()
        try:
            act_title = self.driver.title
            exp_title = "STORE"
            if act_title == exp_title:
                # self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_X_MARK).click()
                self.logger.info("----- Test case 003 is Passed------------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_003_about_us_page.png")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_003_about_us_page",
                              attachment_type=AttachmentType.PNG)
                self.logger.error("----- Test case 003 is Failed--------------")
                assert False
        except TimeoutException as e:
            print(e)
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_003_about_us_page.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_case_003_about_us_page",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("----- Test case 003 is  not executed (Failed)--------------")
            assert False

    @pytest.mark.regression
    @allure.severity(allure.severity_level.MINOR)
    def test_case_004_validate_clicking_on_video_button(self, setup_and_teardown):
        self.logger.info("-----test_case_004_validate_clicking_on_video_button--------------")
        self.logger.info("-----Verifying clicking_on_video_button----------------")
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
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_004_about_us_page.png")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_004_about_us_page",
                              attachment_type=AttachmentType.PNG)
                self.logger.error("----- Test case 004 is Failed--------------")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_004_about_us_page.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_case_004_about_us_page",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("----- Test case 004 is Failed--------------")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.severity(allure.severity_level.MINOR)
    def test_case_005_validate_video_pause_button(self, setup_and_teardown):
        self.logger.info("-----test_case_005_validate_video_pause_button--------------")
        self.logger.info("-----Verifying video_pause_button----------------")
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
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_005_about_us_page.png")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_005_about_us_page",
                              attachment_type=AttachmentType.PNG)
                self.logger.error("----- Test case 005 is Failed-----")
                assert False
        except TimeoutException as e:
            print(e)
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_005_about_us_page.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_case_005_about_us_page",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("----- Test case 005 is Failed--------------")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.severity(allure.severity_level.MINOR)
    def test_case_006_validate_video_volume_mute_button(self, setup_and_teardown):
        self.logger.info("-----test_case_006_validate_video_volume_mute_button--------------")
        self.logger.info("-----Verifying video_volume_mute_button----------------")
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
                    self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_006_about_us_page.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_case_006_about_us_page",
                                  attachment_type=AttachmentType.PNG)
                    self.logger.error("----- Test case 006 is Failed-----")
                    assert False
        except TimeoutException as e:
            print(e)
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_006_about_us_page.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_case_006_about_us_page",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("----- Test case 006 is Failed--------------")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.severity(allure.severity_level.MINOR)
    def test_case_007_validate_video_picture_in_picture_button(self, setup_and_teardown):
        self.logger.info("-----test_case_007_validate_video_picture_in_picture_button--------------")
        self.logger.info("-----Verifying video_picture_in_picture_button----------------")
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
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_007_about_us_page.png")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_007_about_us_page",
                              attachment_type=AttachmentType.PNG)
                self.logger.error("----- Test case 007 is Failed-----")
                assert False
        except TimeoutException as e:
            print(e)
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_007_about_us_page.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_case_007_about_us_page",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("----- Test case 007 is Failed--------------")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.severity(allure.severity_level.MINOR)
    def test_case_008_validate_video_full_screen_button(self, setup_and_teardown):
        self.logger.info("-----test_case_008_validate_video_full_screen_button--------------")
        self.logger.info("-----Verifying video_full_screen_button----------------")
        self.driver = setup_and_teardown
        self.abt_page = About_us_Page(self.driver)
        self.abt_page.click_on_full_screen_button()
        try:
            # is_displayed = self.driver.find_element(By.XPATH, self.non_full_screen).is_displayed()
            message = self.driver.find_element(By.XPATH, self.non_full_screen).text
            print(message)
            # if is_displayed:
            if message == "Non-Fullscreen..":
                self.logger.info("----- Test case 008 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_008_about_us_page.png")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_008_about_us_page",
                              attachment_type=AttachmentType.PNG)
                self.logger.error("----- Test case 008 is Failed-----")
                assert False
        except TimeoutException as e:
            print(e)
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_008_about_us_page.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_case_008_about_us_page",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("----- Test case 008 is Failed--------------")
            assert False
