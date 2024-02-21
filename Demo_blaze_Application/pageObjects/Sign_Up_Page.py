import json

from selenium.webdriver.common.by import By


class Sign_Up_Page:

    json_file_path = "./Locators/locators.json"
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    SIGN_UP_BUTTON = data["Sign_Up_Page"]["SIGN_UP_BUTTON"]
    USERNAME = data["Sign_Up_Page"]["USERNAME"]
    PASSWORD = data["Sign_Up_Page"]["PASSWORD"]
    SIGN_UP_BUTTON_TO_PROCEED = data["Sign_Up_Page"]["SIGN_UP_BUTTON_TO_PROCEED"]
    SIGN_UP_CLOSE_BUTTON = data["Sign_Up_Page"]["SIGN_UP_CLOSE_BUTTON"]
    SIGN_UP_X_MARK = data["Sign_Up_Page"]["SIGN_UP_X_MARK"]

    def __init__(self, driver):
        self.driver = driver

    def click_on_sign_up_button(self):
        self.driver.find_element(By.XPATH, self.SIGN_UP_BUTTON).click()

    def set_sign_up_username_and_password(self, username, password):
        self.driver.find_element(By.XPATH, self.SIGN_UP_BUTTON).click()
        self.driver.find_element(By.XPATH, self.USERNAME).clear()
        self.driver.find_element(By.XPATH, self.USERNAME).send_keys(username)
        self.driver.find_element(By.XPATH, self.PASSWORD).clear()
        self.driver.find_element(By.XPATH, self.PASSWORD).send_keys(password)
        self.driver.find_element(By.XPATH, self.SIGN_UP_BUTTON_TO_PROCEED).click()

    def click_on_sign_up_close_button(self):
        self.driver.find_element(By.XPATH, self.SIGN_UP_BUTTON).click()
        self.driver.find_element(By.XPATH, self.SIGN_UP_CLOSE_BUTTON).click()

    def click_on_sign_up_x_mark_to_close(self):
        self.driver.find_element(By.XPATH, self.SIGN_UP_BUTTON).click()
        self.driver.find_element(By.XPATH, self.SIGN_UP_X_MARK).click()






