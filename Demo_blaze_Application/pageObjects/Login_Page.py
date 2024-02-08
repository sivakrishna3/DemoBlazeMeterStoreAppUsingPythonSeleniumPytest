import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:
    Login_Button = "//a[@id='login2' and contains(text(),'Log in')]"
    Login_Username_text = "//input[@id='loginusername']"
    Login_Password_text = "//input[@id='loginpassword']"
    Login_button_proceed = "//button[@onclick='logIn()' and contains(text(),'Log in')]"
    Login_close_button = "//*[@id='logInModal']/div/div/div[3]/button[1]"
    Logout_Button = "//a[@id='logout2']"
    Welcome_button = "//a[@id='nameofuser']"

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
        self.driver.find_element(By.XPATH, self.Logout_Button).click()
