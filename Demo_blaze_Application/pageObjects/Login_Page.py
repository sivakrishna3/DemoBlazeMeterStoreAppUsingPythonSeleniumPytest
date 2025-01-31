from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig


class LoginPage:

    data = ReadConfig.get_json_data()
    try:
        Login_Button = data["Login_Page"]["Login_Button"]
        Login_Username_text = data["Login_Page"]["Login_Username_text"]
        Login_Password_text = data["Login_Page"]["Login_Password_text"]
        Login_button_proceed = data["Login_Page"]["Login_button_proceed"]
        Login_close_button = data["Login_Page"]["Login_close_button"]
        Logout_Button = data["Login_Page"]["Logout_Button"]
        Welcome_button = data["Login_Page"]["Welcome_button"]
    except Exception as e:
        print(f"{e}: No such element found in json file.")

    def __init__(self, driver):
        self.driver = driver

    def set_username_and_password(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.title_is("STORE"))
        self.driver.find_element(By.XPATH, self.Login_Button).click()
        self.driver.find_element(By.XPATH, self.Login_Username_text).clear()
        self.driver.find_element(By.XPATH, self.Login_Username_text).send_keys(username)
        self.driver.find_element(By.XPATH, self.Login_Password_text).clear()
        self.driver.find_element(By.XPATH, self.Login_Password_text).send_keys(password)
        self.driver.find_element(By.XPATH, self.Login_button_proceed).click()

    # def click_login_button(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.visibility_of_element_located(self.driver.find_element(By.XPATH,self.Login_button_proceed)))

    def click_on_logout_button(self, username, password):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.Logout_Button)))
        self.driver.find_element(By.XPATH, self.Login_Button).click()
        self.driver.find_element(By.XPATH, self.Login_Username_text).clear()
        self.driver.find_element(By.XPATH, self.Login_Username_text).send_keys(username)
        self.driver.find_element(By.XPATH, self.Login_Password_text).clear()
        self.driver.find_element(By.XPATH, self.Login_Password_text).send_keys(password)
        self.driver.find_element(By.XPATH, self.Login_button_proceed).click()
        # self.driver.find_element(By.XPATH, self.Logout_Button).click()

    # def click_on_log_out_in_DDT(self):
    #     self.driver.find_element(By.XPATH, self.Logout_Button).click()
