import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilities.custom_Logger import Log_Generator
from pageObjects.Login_Page import LoginPage
from utilities import Excel_Utils
from utilities.readProperties import ReadConfig


@allure.description("validate_Login_button_with_Data_Driven_Test")
@allure.severity(allure.severity_level.BLOCKER)
class Test_case_001_DDT:
    data = ReadConfig.get_json_data()
    try:
        Login_Button = data["Login_Page"]["Login_Button"]
        CLOSE_BUTTON = data["Login_Page"]["CLOSE_BUTTON"]
        Login_Username_text = data["Login_Page"]["Login_Username_text"]
        Login_Password_text = data["Login_Page"]["Login_Password_text"]
        Login_button_proceed = data["Login_Page"]["Login_button_proceed"]
        Logout_Button = data["Login_Page"]["Logout_Button"]
    except Exception as e:
        print(f"{e} No such element found in json file.")

    logger = Log_Generator.log_gen()
    read_data = Excel_Utils.read_data()

    @allure.description("Login test with Data Driven Test...")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_001_login_data_driven_test(self, setup_and_teardown):
        self.logger.info("-----test_case_001_login_data_driven_test-----")
        self.logger.info("-----Verifying log in functionality-----")
        self.driver = setup_and_teardown
        self.lg_page = LoginPage(self.driver)
        self.rows = Excel_Utils.get_row_count(Excel_Utils.get_row_count('Login_Data'))
        print("Number of rows in a Excel : ", self.rows)

        lst_status = []
        for row in self.read_data:
            self.driver.refresh()
            self.lg_page.set_username_and_password(row[0] if row[0] is not None else '',
                                                   row[1] if row[1] is not None else '')
            self.expected_result = row[2]
            time.sleep(3)
            try:
                is_displayed = self.driver.find_element(By.XPATH, self.Logout_Button).is_displayed()
                if is_displayed:
                    self.driver.find_element(By.XPATH, self.Logout_Button).click()
                    time.sleep(5)
                    act_title = self.driver.title
                    exp_title = "STORE"
                    try:
                        if act_title == exp_title:
                            if self.expected_result == "Pass":
                                self.logger.info("-----Login successful and test case Passed----")
                                lst_status.append("Pass")
                            elif self.expected_result == "Fail":
                                self.logger.error("-----Failed-----")
                                lst_status.append("Fail")
                    except TimeoutError:
                        time.sleep(5)
                        self.driver.save_screenshot(".\\ScreenShots\\Login_with_DataDrivenTest.png")
                        allure.attach(self.driver.get_screenshot_as_png(), name="Login_with_DataDrivenTest",
                                      attachment_type=AttachmentType.PNG)
                        self.logger.error("----Login test of DDT is Failed-----")

                else:
                    wait = WebDriverWait(self.driver, 10)
                    wait.until(EC.alert_is_present())
                    act_text = self.driver.switch_to.alert
                    actual_message = act_text.text
                    print(actual_message)
                    self.driver.switch_to.alert.accept()
                    time.sleep(5)
                    self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
                    # self.driver.refresh()
                    time.sleep(5)
                    expected_message = ["User does not exist.", "Wrong password.",
                                        "Please fill out Username and Password."]
                    act_title = self.driver.title
                    exp_title = "STORE"
                    try:
                        if actual_message == expected_message and act_title == exp_title:
                            if self.expected_result == "Fail":
                                self.logger.info("-----Login successful and test case is Passed----")
                                self.driver.save_screenshot(".\\ScreenShots\\login_with_ddt.png")
                                allure.attach(self.driver.get_screenshot_as_png(), name="Login_with_DataDrivenTest",
                                              attachment_type=AttachmentType.PNG)
                                lst_status.append("Pass")
                            elif self.expected_result == "Pass":
                                self.logger.error("-----Failed-----")
                                lst_status.append("Fail")
                    except TimeoutError:
                        time.sleep(5)
                        self.logger.error("----Login test of DDT is Failed-----")
            except Exception as e:
                print(f"Exception Error : {e}")
        print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("-----Login test DDT is Passed-----")
            assert True
        else:
            time.sleep(5)
            self.logger.error("----Login test of DDT is Failed-----")
            assert False
