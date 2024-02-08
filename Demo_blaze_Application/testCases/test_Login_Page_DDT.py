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

    logger = Log_Generator.log_gen()

    def test_case_001_login_data_driven_test(self, setup_and_teardown):
        self.logger.info("-----test_case_001_login_data_driven_test-----")
        self.logger.info("-----Verifying log in functionality-----")
        self.driver = setup_and_teardown
        self.lg_page = LoginPage(self.driver)
        self.rows = Excel_Utils.get_row_count(self.file_path, 'Login_Data')
        print("Number of rows in a Excel : ", self.rows)

        lst_status = []
        for row in range(2, self.rows+1):
            self.username = Excel_Utils.read_data(self.file_path, 'Login_Data', row, 2)
            self.password = Excel_Utils.read_data(self.file_path, 'Login_Data', row, 3)
            self.expected_result = Excel_Utils.read_data(self.file_path, 'Login_Data', row, 4)

            self.lg_page.set_username_and_password(self.username, self.password)
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.alert_is_present())
            act_text = self.driver.switch_to.alert
            actual_message = act_text.text
            print(actual_message)
            self.driver.switch_to.alert.accept()
            self.driver.find_element(By.XPATH, self.CLOSE_BUTTON).click()
            time.sleep(5)
            expected_message = ["User does not exist.", "Wrong password.", "Please fill out Username and Password."]
            act_title = self.driver.title
            exp_title = "STORE"

            if actual_message == expected_message or act_title == exp_title:
                if self.expected_result == "Pass":
                    self.logger.info("----Login successful and test case is Passed----")
                    self.lg_page.click_on_logout_button()
                    lst_status.append("Pass")
                elif self.expected_result == "Fail":
                    self.logger.error("----Failed-----")
                    lst_status.append("Fail")

            elif actual_message != expected_message:
                if self.expected_result == "Pass":
                    self.logger.error("-----Failed---------")
                    lst_status.append("Fail")
                elif self.expected_result == "Fail":
                    self.logger.info("----Passed-----")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("-----Login test DDT is Passed-----")
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\login_with_ddt.png")
            self.logger.error("----Login test of DDT is Failed")
            assert False
