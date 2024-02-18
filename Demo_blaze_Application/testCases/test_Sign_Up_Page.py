import random
import string
import time

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.Sign_Up_Page import Sign_Up_Page
from utilities.custom_Logger import Log_Generator
from utilities.readProperties import ReadConfig


class TestCase006SignUpPage:

    def generate_random_email(self):
        random_username = ''.join(random.choices(string.ascii_letters.lower(), k=8))
        return f'{random_username}@gmail.com'

    valid_username = ReadConfig.get_sign_up_username()
    invalid_username = ReadConfig.get_sign_up_invalid_username()
    username_with_space = ReadConfig.get_sign_up_username_with_space()
    username_with_spl_chars = ReadConfig.get_sign_up_username_with_spl_chars()
    username_with_numbers = ReadConfig.get_sign_up_username_with_numbers()
    no_username = ReadConfig.get_sign_up_no_username()
    valid_password = ReadConfig.get_sign_up_password()
    invalid_password = ReadConfig.get_sign_up_invalid_password()
    password_with_space = ReadConfig.get_sign_up_password_with_space()
    password_with_spl_chars = ReadConfig.get_sign_up_password_with_spl_chars()
    password_with_numbers = ReadConfig.get_sign_up_password_with_numbers()
    no_password = ReadConfig.get_sign_up_no_password()

    SIGN_UP_PAGE_TITLE = "//h5[@id='signInModalLabel' and contains(text(),'Sign up')]"
    logger = Log_Generator.log_gen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_cse_001_validate_sign_up_button(self, setup_and_teardown):
        self.logger.info("-----test_cse_001_validate_sign_up_button------")
        self.logger.info("-----Verifying Sign Up Page------")
        self.driver = setup_and_teardown
        self.sg_page = Sign_Up_Page(self.driver)
        self.sg_page.click_on_sign_up_button()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.SIGN_UP_PAGE_TITLE)))
            actual_text = self.driver.find_element(By.XPATH, self.SIGN_UP_PAGE_TITLE).text
            expected_text = "Sign up"
            if actual_text == expected_text:
                self.logger.info("-----test case 001 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.logger.error("-----TimeoutException: Sign up page not displayed------")
                self.driver.save_screenshot(".\\ScreenShots\\Sign_Up_Page\\" + "test_case_001_timeout.png")
                assert False

        except TimeoutException:
            self.logger.error("-----TimeoutException: Sign up page not displayed------")
            self.driver.save_screenshot(".\\ScreenShots\\Sign_Up_Page\\" + "test_case_001_timeout.png")
            print("TimeoutException: Sign up page not displayed")
        except AssertionError as e:
            self.logger.error(f"-----AssertionError: {e}------")
            self.driver.save_screenshot(".\\ScreenShots\\Sign_Up_Page\\" + "test_case_001_failure.png")
            print(f"AssertionError: {e}")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_002_validate_sign_up_with_valid_username_valid_password(self, setup_and_teardown):
        self.valid_random_username = self.generate_random_email()
        self.logger.info("-----test_case_002_validate_sign_up_with_valid_username_valid_password------")
        self.logger.info("-----Verifying Sign Up Page------")
        self.driver = setup_and_teardown
        self.sg_page = Sign_Up_Page(self.driver)
        self.sg_page.set_sign_up_username_and_password(self.valid_random_username, self.valid_password)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        expected_message = "Sign up successful."
        print(self.valid_random_username)
        try:
            if actual_message == expected_message:
                self.logger.info("--------test case 002 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Sign_Up_Page\\" + "test_case_002.png")
                self.logger.error("--------test case 002 is Failed--------")
                assert False
        except Exception as e:
            print(e)
            self.driver.save_screenshot(".\\ScreenShots\\Sign_Up_Page\\" + "test_case_002.png")
            self.logger.error("--------Sign up with valid username and valid password is Failed---------")
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_003_validate_sign_up_with_invalid_username_invalid_password(self, setup_and_teardown):
        self.logger.info("-----test_case_003_validate_sign_up_with_invalid_username_invalid_password------")
        self.logger.info("-----Verifying Sign Up Page------")
        self.driver = setup_and_teardown
        self.sg_page = Sign_Up_Page(self.driver)
        self.sg_page.set_sign_up_username_and_password(self.invalid_username, self.invalid_password)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        expected_message = "Sign up successful."
        try:
            if actual_message != expected_message:
                self.logger.info("--------test case 003 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Sign_Up_Page\\" + "test_case_003.png")
                self.logger.error("--------test case 003 is Failed--------")
                assert False
        except Exception as e:
            print(e)
            self.driver.save_screenshot(".\\ScreenShots\\Sign_Up_Page\\" + "test_case_003.png")
            self.logger.error("--------Sign up with invalid username and invalid password is Failed---------")

            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_004_validate_sign_up_username_with_space_and_password_with_space(self, setup_and_teardown):
        self.logger.info("-----test_case_004_validate_sign_up_username_with_space_and_password_with_space------")
        self.logger.info("-----Verifying Sign Up Page------")
        self.driver = setup_and_teardown
        self.sg_page = Sign_Up_Page(self.driver)
        self.sg_page.set_sign_up_username_and_password(self.username_with_space, self.password_with_space)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        expected_message = "Sign up successful."
        try:
            if actual_message != expected_message:
                self.logger.info("--------test case 004 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Sign_Up_Page\\" + "test_case_004.png")
                self.logger.error("--------test case 004 is Failed--------")
                assert False
        except Exception as e:
            print(e)
            self.driver.save_screenshot(".\\ScreenShots\\Sign_Up_Page\\" + "test_case_004.png")
            self.logger.error("--------Sign up username with space and password with space is Failed---------")
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_005_validate_sign_up_username_with_spl_chars_and_password_with_spl_chars(self, setup_and_teardown):
        self.logger.info("-----test_case_005_validate_sign_up_username_with_spl_chars_and_password_with_spl_chars------")
        self.logger.info("-----Verifying Sign Up Page------")
        self.driver = setup_and_teardown
        self.sg_page = Sign_Up_Page(self.driver)
        self.sg_page.set_sign_up_username_and_password(self.username_with_spl_chars, self.password_with_spl_chars)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        expected_message = "Sign up successful."
        try:
            if actual_message != expected_message:
                self.logger.info("--------test case 005 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Sign_Up_Page\\" + "test_case_005.png")
                self.logger.error("--------test case 005 is Failed--------")
                assert False
        except Exception as e:
            print(e)
            self.driver.save_screenshot(".\\ScreenShots\\Sign_Up_Page\\" + "test_case_005.png")
            self.logger.error("--------Sign up username with spl chars and password with spl chars is Failed---------")
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_006_validate_sign_up_username_with_numbers_and_password_with_numbers(self, setup_and_teardown):
        self.valid_random_username = self.generate_random_email()
        self.logger.info("-----test_case_006_validate_sign_up_username_with_numbers_and_password_with_numbers------")
        self.logger.info("-----Verifying Sign Up Page------")
        self.driver = setup_and_teardown
        self.sg_page = Sign_Up_Page(self.driver)
        self.sg_page.set_sign_up_username_and_password(self.username_with_numbers, self.password_with_numbers)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        expected_message = "Sign up successful."
        try:
            if actual_message != expected_message:
                self.logger.info("--------test case 006 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Sign_Up_Page\\" + "test_case_006.png")
                self.logger.error("--------test case 006 is Failed--------")
                assert False
        except Exception as e:
            print(e)
            self.driver.save_screenshot(".\\ScreenShots\\Sign_Up_Page\\" + "test_case_006.png")
            self.logger.error("--------Sign up username with numbers and password with numbers is Failed---------")
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_007_validate_sign_up_with_no_username_and_no_password(self, setup_and_teardown):
        self.logger.info("-----test_case_007_validate_sign_up_with_no_username_and_no_password------")
        self.logger.info("-----Verifying Sign Up Page------")
        self.driver = setup_and_teardown
        self.sg_page = Sign_Up_Page(self.driver)
        self.sg_page.set_sign_up_username_and_password(self.no_username, self.no_password)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        expected_message = "Sign up successful."
        try:
            if actual_message != expected_message:
                self.logger.info("--------test case 007 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Sign_Up_Page\\" + "test_case_007.png")
                self.logger.error("--------test case 007 is Failed--------")
                assert False
        except Exception as e:
            print(e)
            self.driver.save_screenshot(".\\ScreenShots\\Sign_Up_Page\\" + "test_case_007.png")
            self.logger.error("--------Sign up with no username and no password is Failed---------")
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_cse_008_validate_clicking_on_sign_up_close_button(self, setup_and_teardown):
        self.logger.info("-----test_cse_008_validate_clicking_on_sign_up_close_button------")
        self.logger.info("-----Verifying Sign Up Page------")
        self.driver = setup_and_teardown
        self.sg_page = Sign_Up_Page(self.driver)
        self.sg_page.click_on_sign_up_close_button()
        act_title = self.driver.title
        exp_title = "STORE"
        try:
            if act_title == exp_title:
                self.logger.info("--------test case 008 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Sign_Up_Page\\" + "test_case_008.png")
                self.logger.error("--------test case 008 is Failed--------")
                assert False
        except Exception as e:
            print(e)
            self.driver.save_screenshot(".\\ScreenShots\\Sign_Up_Page\\" + "test_case_009.png")
            self.logger.error("-------Clicking on sign up close button is Failed---------")
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_cse_009_validate_clicking_on_sign_up_x_mark(self, setup_and_teardown):
        self.logger.info("-----test_cse_009_validate_clicking_on_sign_up_x_mark------")
        self.logger.info("-----Verifying Sign Up Page------")
        self.driver = setup_and_teardown
        self.sg_page = Sign_Up_Page(self.driver)
        self.sg_page.click_on_sign_up_close_button()
        act_title = self.driver.title
        exp_title = "STORE"
        try:
            if act_title == exp_title:
                self.logger.info("--------test case 009 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Sign_Up_Page\\" + "test_case_009.png")
                self.logger.error("--------test case 009 is Failed--------")
                assert False
        except Exception as e:
            print(e)
            self.driver.save_screenshot(".\\ScreenShots\\Sign_Up_Page\\" + "test_case_009.png")
            self.logger.error("-------Clicking on sign up close button is Failed---------")
            assert False
