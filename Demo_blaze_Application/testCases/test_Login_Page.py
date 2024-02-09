# import pytest
# from selenium.webdriver import Chrome
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageObjects.Login_Page import LoginPage
from utilities.readProperties import ReadConfig
from utilities.custom_Logger import Log_Generator


class TestCase001LoginPage:
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
    CLOSE_BUTTON = "//*[@id='logInModal']/div/div/div[3]/button[1]"
    expected_message = ["User does not exist.", "Wrong password.", "Please fill out Username and Password."]
    logger = Log_Generator.log_gen()

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
                self.logger.info("-----Login with valid username and valid password is Passed---------")
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_001.png")
                self.logger.error("-------Login with valid username and valid password is Failed-----")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login with valid username and invalid password is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_002.png")
                self.logger.error("-----Login with valid username and invalid password is Failed--------------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("--------Login with valid username and password with spl chars is Passed-----------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_003.png")
                self.logger.error("--------Login with valid username and password with spl chars i is Failed---------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("---------Login with valid username and password with numbers is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_004.png")
                self.logger.error("---------Login with valid username and password with numbers is Failed-----------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login with valid username and password with space is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_005.png")
                self.logger.error("-----Login with valid username and password with space is Failed--------------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login with valid username and no password is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_006.png")
                self.logger.error("-----Login with valid username and no password is Failed--------------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login with invalid username and valid password is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_007.png")
                self.logger.error("-----Login invalid username and valid password is Failed--------------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login  with invalid username and invalid password is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_008.png")
                self.logger.error("-----Login with invalid username and invalid password is Failed--------------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("--------Login with invalid username and password with spl chars is Passed----------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_009.png")
                self.logger.error("--------Login with invalid username and password with spl chars is Failed--------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("--------Login with invalid username and password with numbers is Passed-----------")

                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_010.png")
                self.logger.error("-------Login with invalid username and password with numbers is Failed-----------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login with invalid username and password with space is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_011.png")
                self.logger.error("-----Login with invalid username and password with space is Failed--------------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login with invalid username and no password is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_012.png")
                self.logger.error("-----Login with invalid username and no password is Failed--------------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login username with space and valid password is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_013.png")
                self.logger.error("-----Login username with space and valid password is Failed--------------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login username with space and invalid password is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_014.png")
                self.logger.error("-----Login username with space and invalid password is Failed--------------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-------Login username with space and password with spl chars is Passed------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_015.png")
                self.logger.error("-------Login username with space and password with spl chars is Failed-----------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login username with space and password with numbers is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_016.png")
                self.logger.error("-----Login username with space and password with numbers is Failed--------------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login username with space and password with space is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_017.png")
                self.logger.error("-----Login username with space and password with space is Failed--------------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login username with space and no password is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_018.png")
                self.logger.error("-----Login username with space and no password is Failed--------------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-------Login username with spl chars and valid password is Passed-----------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_019.png")
                self.logger.error("-------Login username with spl chars and valid password is Failed--------------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login username with spl chars and invalid password is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_020.png")
                self.logger.error("-----Login username with spl chars and invalid password is Failed---------")
                assert False
        except Exception as e:
            print(e)

    def test_case_021_validate_login_username_with_spl_chars_and_password_with_spl_chars(self, setup_and_teardown):
        self.logger.info("-----test_case_021_validate_login_username_with_spl_chars_and_password_with_spl_chars-----------")
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
                self.logger.info("-------Login username with spl chars and password with spl chars is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_021.png")
                self.logger.error("------Login username with spl chars and password with spl chars is Failed-----")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login username with spl chars and password with numbers is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_022.png")
                self.logger.error("-----Login username with spl chars and password with numbers is Failed---------")
                assert False
        except Exception as e:
            print(e)

    def test_case_023_validate_login_username_with_spl_chars_and_password_with_space(self, setup_and_teardown):
        self.logger.info("-----test_case_023_validate_login_username_with_spl_chars_and_password_with_space-----------")
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
                self.logger.info("-----Login username with spl chars and password with space is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_023.png")
                self.logger.error("-----Login username with spl chars and password with space is Failed---------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login username with space and no password is Passed--------------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_024.png")
                self.logger.error("-----Login username with space and no password is Failed--------------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login username with numbers and valid password is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_025.png")
                self.logger.error("-----Login username with numbers and valid password is Failed---------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login username with numbers and invalid password is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_026.png")
                self.logger.error("-----Login username with numbers and invalid password is Failed---------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login username with numbers and password with spl chars is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_027.png")
                self.logger.error("-----Login username with numbers and password with spl chars is Failed---------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login username with numbers and password with numbers is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_028.png")
                self.logger.error("-----Login username with numbers and password with numbers is Failed---------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login username with numbers and password with space is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_029.png")
                self.logger.error("-----Login username with numbers and password with space is Failed---------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login username with numbers and no password is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_030.png")
                self.logger.error("-----Login username with numbers and no password is Failed---------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login with no username and valid password is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_031.png")
                self.logger.error("-----Login with no username and valid password is Failed---------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login with no username and invalid password is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_032.png")
                self.logger.error("-----Login with no username and invalid password is Failed---------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login with no username and password with spl chars is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_033.png")
                self.logger.error("-----Login with no username and password with spl chars is Failed---------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login with no username and password with numbers is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_034.png")
                self.logger.error("-----Login with no username and password with numbers is Failed---------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login with no username and password with space is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_035.png")
                self.logger.error("-----Login with no username and password with space is Failed---------")
                assert False
        except Exception as e:
            print(e)

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
                self.logger.info("-----Login with no username and no password is Passed---------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Login_Page\\" + "test_case_036.png")
                self.logger.error("-----Login with no username and no password is Failed---------")
                assert False
        except Exception as e:
            print(e)

    def test_case_037_validate_logout_button(self, setup_and_teardown):
        self.logger.info("-----test_case_037_validate_logout_button-----------")
        self.logger.info("-----Verifying Logout functionality--------")
        self.driver = setup_and_teardown
        self.lgn_page = LoginPage(self.driver)
        self.lgn_page.click_on_logout_button(self.valid_username, self.valid_password)
        act_title = self.driver.title
        try:
            if act_title == "STORE":
                self.logger.info("-----Log out functionality is Passed------------------")
                assert True
            else:
                time.sleep(5)
                self.logger.error("-----Log out functionality is Failed------------------")
                assert False
        except Exception as e:
            print(e)
