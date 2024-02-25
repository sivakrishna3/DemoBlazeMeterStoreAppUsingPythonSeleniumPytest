import json

import pytest
# from selenium.webdriver import Chrome
import time

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageObjects.Login_Page import LoginPage
from utilities.readProperties import ReadConfig
from utilities.custom_Logger import Log_Generator


class TestCase001LoginPage:
    try:
        valid_username = ReadConfig.get_username()
        valid_password = ReadConfig.get_password()
        invalid_username = ReadConfig.get_invalid_username()
        invalid_password = ReadConfig.get_invalid_password()
        no_username = ReadConfig.get_no_username()
        no_password = ReadConfig.get_no_password()
        username_with_spl_chars = ReadConfig.get_username_with_spl_chars()
        password_with_spl_chars = ReadConfig.get_password_with_spl_chars()
        username_with_space = ReadConfig.get_username_with_space()
        password_with_space = ReadConfig.get_password_with_space()
        username_with_numbers = ReadConfig.get_username_with_numbers()
        password_with_numbers = ReadConfig.get_password_with_numbers()
    except Exception as e:
        print(f"{e}: No such element found in ini file.")

    data = ReadConfig.get_json_data()
    try:
        CLOSE_BUTTON = data["Login_Page"]["CLOSE_BUTTON"]
        Logout_Button = data["Login_Page"]["Logout_Button"]
        expected_message = ["User does not exist.", "Wrong password.", "Please fill out Username and Password."]
        logger = Log_Generator.log_gen()
    except Exception as e:
        print(f"{e}: No such element found in json file.")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_001_validate_login_with_valid_username_valid_password(self, setup_and_teardown):
        self.logger.info("-----test_case_001_validate_login_with_valid_username_valid_password-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.valid_username, self.valid_password)
        act_title = self.driver.title
        print(act_title)
        try:
            if act_title == 'STORE':
                assert True
                self.logger.info("-----Test case 001 is Passed---------")
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_001_login_page.png")
                self.logger.error("-----Test case 001 is Failed-----")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_002_validate_login_with_valid_username_invalid_password(self, setup_and_teardown):
        self.logger.info("-----test_case_002_validate_login_with_valid_username_invalid_password-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.valid_username, self.invalid_password)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 002 is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_002_login_page.png")
                self.logger.error("-----Test case 002 is Failed--------------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_003_validate_login_with_valid_username_password_with_spl_chars(self, setup_and_teardown):
        self.logger.info("-----test_case_003_validate_login_with_valid_username_password_with_spl_chars-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.valid_username, self.password_with_spl_chars)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 003 is Passed-----------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_003_login_page.png")
                self.logger.error("-----Test case 003 is Failed---------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_004_validate_login_with_valid_username_password_with_numbers(self, setup_and_teardown):
        self.logger.info("-----test_case_004_validate_login_with_valid_username_password_with_numbers-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.valid_username, self.password_with_numbers)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("------Test case 004 is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_004_login_page.png")
                self.logger.error("------Test case 004 is Failed-----------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_005_validate_login_with_valid_username_password_with_space(self, setup_and_teardown):
        self.logger.info("-----test_case_005_validate_login_with_valid_username_password_with_space-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.valid_username, self.password_with_space)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 005 is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_005_login_page.png")
                self.logger.error("-----Test case 005 is Failed--------------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_006_validate_login_with_valid_username_no_password(self, setup_and_teardown):
        self.logger.info("-----test_case_006_validate_login_with_valid_username_no_password-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.valid_username, self.no_password)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 006 is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_006_login_page.png")
                self.logger.error("-----Test case 006 is Failed--------------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_007_validate_login_with_invalid_username_valid_password(self, setup_and_teardown):
        self.logger.info("-----test_case_007_validate_login_with_invalid_username_valid_password-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.invalid_username, self.valid_password)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 007 is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_007_login_page.png")
                self.logger.error("-----Test case 007 is Failed--------------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_008_validate_login_invalid_username_and_invalid_password(self, setup_and_teardown):
        self.logger.info("-----test_case_008_validate_login_invalid_username_and_invalid_password-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.invalid_username, self.invalid_password)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 008 is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_008_login_page.png")
                self.logger.error("-----Test case 008 is Failed--------------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_009_validate_login_with_invalid_username_and_password_with_spl_chars(self, setup_and_teardown):
        self.logger.info("-----test_case_009_validate_login_with_invalid_username_and_password_with_spl_chars--------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.invalid_username, self.password_with_spl_chars)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 009 is Passed----------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_009_login_page.png")
                self.logger.error("-----Test case 009 is Failed--------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_010_validate_login_invalid_username_and_password_with_numbers(self, setup_and_teardown):
        self.logger.info("-----test_case_010_validate_login_invalid_username_and_password_with_numbers-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.username_with_space, self.password_with_numbers)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 010 is Passed-----------")

                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_010_login_page.png")
                self.logger.error("-------Test case 010 is Failed-----------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_011_validate_login_with_invalid_username_and_password_with_space(self, setup_and_teardown):
        self.logger.info("-----test_case_011_validate_login_with_valid_username_and_password_with_space-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.invalid_username, self.password_with_space)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 011 is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_011_login_page.png")
                self.logger.error("-----Test case 011 is Failed--------------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_012_validate_login_with_invalid_username_and_no_password(self, setup_and_teardown):
        self.logger.info("-----test_case_012_validate_login_with_invalid_username_and_no_password-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.invalid_username, self.no_password)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 012 is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_012_login_page.png")
                self.logger.error("-----Test case 012 is Failed--------------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_013_validate_login_with_username_with_space_and_valid_password(self, setup_and_teardown):
        self.logger.info("-----test_case_013_validate_login_with_username_with_space_and_valid_password-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.username_with_space, self.valid_password)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 013 is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_013_login_page.png")
                self.logger.error("-----Test case 013 is Failed--------------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_014_validate_login_with_username_with_space_and_invalid_password(self, setup_and_teardown):
        self.logger.info("-----test_case_014_validate_login_with_username_with_invalid_password-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.username_with_space, self.invalid_password)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 014 is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_014_login_page.png")
                self.logger.error("-----Test case 014 is Failed--------------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_015_validate_login_with_username_with_space_and_password_with_spl_chars(self, setup_and_teardown):
        self.logger.info("-----test_case_015_validate_login_with_username_with_space_and_password_with_spl_chars------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.username_with_space, self.password_with_spl_chars)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-------Test case 015 is Passed------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_015_login_page.png")
                self.logger.error("-------Test case 015 is Failed-----------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_016_validate_login_with_username_with_space_and_password_with_numbers(self, setup_and_teardown):
        self.logger.info("-----test_case_016_validate_login_with_username_with_space_and_password_with_numbers--------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.username_with_space, self.password_with_numbers)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 016 is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_016_login_page.png")
                self.logger.error("-----Test case 016 is Failed--------------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_017_validate_login_with_username_with_space_and_password_with_space(self, setup_and_teardown):
        self.logger.info("-----test_case_017_validate_login_with_username_with_space_and_password_with_space-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.username_with_space, self.password_with_space)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 017 is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_017_login_page.png")
                self.logger.error("-----Test case 017 is Failed--------------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_018_validate_login_with_username_with_space_and_no_password(self, setup_and_teardown):
        self.logger.info("-----test_case_018_validate_login_with_username_with_space_and_no_password-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.username_with_space, self.no_password)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 018 is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_018_login_page.png")
                self.logger.error("-----Test case 018 is Failed--------------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_019_validate_login_username_with_spl_chars_and_valid_password(self, setup_and_teardown):
        self.logger.info("-----test_case_019_validate_login_username_with_spl_chars_and_valid_password-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.username_with_spl_chars, self.valid_password)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 019 is Passed-----------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_019_login_page.png")
                self.logger.error("-----Test case 019 is Failed--------------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_020_validate_login_username_with_spl_chars_and_invalid_password(self, setup_and_teardown):
        self.logger.info("-----test_case_020_validate_login_username_with_spl_chars_and_invalid_password-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.username_with_spl_chars, self.invalid_password)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 020 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_020_login_page.png")
                self.logger.error("-----Test case 020 is Failed---------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_021_validate_login_username_with_spl_chars_and_password_with_spl_chars(self, setup_and_teardown):
        self.logger.info("-----test_case_021_validate_login_username_with_spl_chars_and_password_with_spl_chars------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.username_with_spl_chars, self.password_with_spl_chars)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 021 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_021_login_page.png")
                self.logger.error("----Test case 021 is Failed-----")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_022_validate_login_username_with_spl_chars_and_password_with_numbers(self, setup_and_teardown):
        self.logger.info("-----test_case_022_validate_login_username_with_spl_chars_and_password_with_numbers---------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.username_with_spl_chars, self.password_with_numbers)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 022 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_022_login_page.png")
                self.logger.error("-----Test case 022 is Failed---------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_023_validate_login_username_with_spl_chars_and_password_with_space(self, setup_and_teardown):
        self.logger.info("-----test_case_023_validate_login_username_with_spl_chars_and_password_with_space------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.username_with_spl_chars, self.password_with_space)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 023 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_023_login_page.png")
                self.logger.error("-----Test case 023 is Failed---------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_024_validate_login_username_with_spl_chars_and_no_password(self, setup_and_teardown):
        self.logger.info("-----test_case_024_validate_login_username_with_spl_chars_and_no_password-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.username_with_space, self.no_password)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 024 is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_024_login_page.png")
                self.logger.error("-----Test case 024 is Failed--------------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_025_validate_login_username_with_numbers_and_valid_password(self, setup_and_teardown):
        self.logger.info("-----test_case_025_validate_login_username_with_numbers_and_valid_password-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.username_with_numbers, self.valid_password)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 025 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_025_login_page.png")
                self.logger.error("-----Test case 025 is Failed---------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_026_validate_login_username_with_numbers_and_invalid_password(self, setup_and_teardown):
        self.logger.info("-----test_case_026_validate_login_username_with_numbers_and_invalid_password-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.username_with_numbers, self.invalid_password)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 026 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_026_login_page.png")
                self.logger.error("-----Test case 026 is Failed---------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_027_validate_login_username_with_numbers_and_password_with_spl_chars(self, setup_and_teardown):
        self.logger.info("-----test_case_027_validate_login_username_with_numbers_and_password_with_spl_chars--------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.username_with_numbers, self.password_with_spl_chars)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 027 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_027_login_page.png")
                self.logger.error("-----Test case 027 is Failed---------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_028_validate_login_username_with_numbers_and_password_with_numbers(self, setup_and_teardown):
        self.logger.info("-----test_case_028_validate_login_username_with_numbers_and_password_with_numbers-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.username_with_numbers, self.password_with_numbers)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 028 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_028_login_page.png")
                self.logger.error("-----Test case 028 is Failed---------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_029_validate_login_username_with_numbers_and_password_with_space(self, setup_and_teardown):
        self.logger.info("-----test_case_029_validate_login_username_with_numbers_and_password_with_space-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.username_with_numbers, self.password_with_space)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 029 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_029_login_page.png")
                self.logger.error("-----Test case 029 is Failed---------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_030_validate_login_username_with_numbers_and_no_password(self, setup_and_teardown):
        self.logger.info("-----test_case_030_validate_login_username_with_numbers_and_no_password-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.username_with_numbers, self.no_password)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 030 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_030_login_page.png")
                self.logger.error("-----Test case 030 is Failed---------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_031_validate_login_with_no_username_and_valid_password(self, setup_and_teardown):
        self.logger.info("-----test_case_031_validate_login_with_no_username_and_valid_password-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.no_username, self.valid_password)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 031 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_031_login_page.png")
                self.logger.error("-----Test case 031 is Failed---------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_032_validate_login_with_no_username_and_invalid_password(self, setup_and_teardown):
        self.logger.info("-----test_case_032_validate_login_with_no_username_and_invalid_password-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.no_username, self.invalid_password)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 032 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_032_login_page.png")
                self.logger.error("-----Test case 032 is Failed---------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_033_validate_login_with_no_username_and_password_with_spl_chars(self, setup_and_teardown):
        self.logger.info("-----test_case_033_validate_login_with_no_username_and_password_with_spl_chars-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.no_username, self.password_with_spl_chars)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 033 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_033_login_page.png")
                self.logger.error("-----Test case 033 is Failed---------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_034_validate_login_with_no_username_and_password_with_numbers(self, setup_and_teardown):
        self.logger.info("-----test_case_034_validate_login_with_no_username_and_password_with_numbers-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.no_username, self.password_with_numbers)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 034 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_034_login_page.png")
                self.logger.error("-----Test case 034 is Failed---------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_035_validate_login_with_no_username_and_password_with_space(self, setup_and_teardown):
        self.logger.info("-----test_case_035_validate_login_with_no_username_and_password_with_space-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.no_username, self.password_with_space)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 035 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_035_login_page.png")
                self.logger.error("-----Test case 035 is Failed---------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_036_validate_login_with_no_username_and_no_password(self, setup_and_teardown):
        self.logger.info("-----test_case_036_validate_login_with_no_username_and_no_password-----------")
        self.logger.info("-----Verifying Login functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.set_username_and_password(self.no_username, self.no_password)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
        try:
            if actual_message in self.expected_message:
                self.logger.info("-----Test case 036 is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_036_login_page.png")
                self.logger.error("-----Test case 036 is Failed---------")
                assert False
        except TimeoutException as e:
            print(e)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_037_validate_logout_button(self, setup_and_teardown):
        self.logger.info("-----test_case_037_validate_logout_button-----------")
        self.logger.info("-----Verifying Logout functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.click_on_logout_button(self.valid_username, self.valid_password)

        try:
            is_displayed = self.driver.find_element(By.XPATH, self.Logout_Button).is_displayed()
            if is_displayed:
                message = self.driver.find_element(By.XPATH, self.Logout_Button).text
                print(message)
                self.driver.find_element(By.XPATH, self.Logout_Button).click()
                if message == "Log out":
                    self.logger.info("-----Test case 037 is Passed------------------")
                    assert True
                else:
                    time.sleep(5)
                    self.logger.error("-----Test case 037 is Failed------------------")
                    assert False
        except TimeoutException as e:
            print(e)
