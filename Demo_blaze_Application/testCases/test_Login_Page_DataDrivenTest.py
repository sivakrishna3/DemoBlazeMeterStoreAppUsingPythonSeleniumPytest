import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilities.custom_Logger import Log_Generator
from pageObjects.Login_Page import LoginPage
from utilities import Excel_Utils


class Test_case_001_DDT:
    file_path = ".\\Test_Data\\Test_Data_for_DDT.xlsx"
    CLOSE_BUTTON = "//*[@id='logInModal']/div/div/div[3]/button[1]"
    HOME_BUTTON = "//a[contains(text(),'Home')]"
    Login_Button = "//a[@id='login2' and contains(text(),'Log in')]"
    Login_Username_text = "//input[@id='loginusername']"
    Login_Password_text = "//input[@id='loginpassword']"
    Login_button_proceed = "//button[@onclick='logIn()' and contains(text(),'Log in')]"
    Logout_Button = "//a[@id='logout2']"

    logger = Log_Generator.log_gen()
    read_data = Excel_Utils.read_data()

    def test_case_001_login_data_driven_test(self, setup_and_teardown):
        self.logger.info("-----test_case_001_login_data_driven_test-----")
        self.logger.info("-----Verifying log in functionality-----")
        self.driver = setup_and_teardown
        self.lg_page = LoginPage(self.driver)
        self.rows = Excel_Utils.get_row_count(self.file_path, 'Login_Data')
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
                                print(lst_status,"passed")
                            elif self.expected_result == "Fail":
                                self.logger.error("-----Failed-----")
                                lst_status.append("Fail")
                    except TimeoutError:
                        time.sleep(5)
                        self.driver.save_screenshot(".\\ScreenShots\\login_with_ddt.png")
                        self.logger.error("----Login test of DDT is Failed-----")

                else:
                    wait = WebDriverWait(self.driver, 10)
                    wait.until(EC.alert_is_present())
                    act_text = self.driver.switch_to.alert
                    actual_message = act_text.text
                    print(actual_message)
                    self.driver.switch_to.alert.accept()
                    time.sleep(5)
                    import pdb; pdb.set_trace()
                    self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
                    # self.driver.refresh()
                    time.sleep(5)
                    expected_message = ["User does not exist.", "Wrong password.",
                                        "Please fill out Username and Password."]
                    act_title = self.driver.title
                    exp_title = "STORE"
                    try:
                        if actual_message == expected_message:
                            if self.expected_result == "Fail":
                                self.logger.info("-----Login successful and test case is Passed----")
                                self.driver.save_screenshot(".\\ScreenShots\\login_with_ddt.png")
                                print(lst_status, "passed2")
                                lst_status.append("Pass")
                            elif self.expected_result == "Pass":
                                self.logger.error("-----Failed-----")
                                lst_status.append("Fail")
                    except TimeoutError:
                        time.sleep(5)
                        self.logger.error("----Login test of DDT is Failed-----")
            except Exception as e:
                print(f"Exception Error : {e}")
        if "Fail" not in lst_status:
            self.logger.info("-----Login test DDT is Passed-----")
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\login_with_ddt.png")
            self.logger.error("----Login test of DDT is Failed-----")
            assert False
