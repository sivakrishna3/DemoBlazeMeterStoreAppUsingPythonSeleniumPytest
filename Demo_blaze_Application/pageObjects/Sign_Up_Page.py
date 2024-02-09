from selenium.webdriver.common.by import By


class Sign_Up_Page:

    SIGN_UP_BUTTON = "//a[@id='signin2']"
    USERNAME = "//input[@id='sign-username']"
    PASSWORD = "//input[@id='sign-password']"
    SIGN_UP_BUTTON_TO_PROCEED = "//*[@id='signInModal']/div/div/div[3]/button[2]"
    SIGN_UP_CLOSE_BUTTON = "//*[@id='signInModal']/div/div/div[3]/button[1]"
    SIGN_UP_X_MARK = "//*[@id='signInModal']/div/div/div[1]/button/span"

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






