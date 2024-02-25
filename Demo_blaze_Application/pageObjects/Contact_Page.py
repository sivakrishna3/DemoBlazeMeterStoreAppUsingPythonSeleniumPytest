# import pytest
# from selenium.webdriver import Chrome
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig


class Contact_page:
    data = ReadConfig.get_json_data()
    try:
        CONTACT_BUTTON = data["Contact_Page"]["CONTACT_BUTTON"]
        CONTACT_EMAIL_TEXT = data["Contact_Page"]["CONTACT_EMAIL_TEXT"]
        CONTACT_NAME_TEXT = data["Contact_Page"]["CONTACT_NAME_TEXT"]
        CONTACT_MESSAGE_TEXT = data["Contact_Page"]["CONTACT_MESSAGE_TEXT"]
        CONTACT_SEND_MESSAGE_BUTTON = data["Contact_Page"]["CONTACT_SEND_MESSAGE_BUTTON"]
        CONTACT_CLOSE_BUTTON = data["Contact_Page"]["CONTACT_CLOSE_BUTTON"]
        CONTACT_X_MARK = data["Contact_Page"]["CONTACT_X_MARK"]
        CONTACT_NEW_MESSAGE_TEXT = data["Contact_Page"]["CONTACT_NEW_MESSAGE_TEXT"]
    except Exception as e:
        print(f"{e}: No such element found in json file.")

    def __init__(self, driver):
        self.driver = driver

    def click_on_contact_button(self):
        self.driver.find_element(By.XPATH, self.CONTACT_BUTTON).click()
        # WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.CONTACT_NEW_MESSAGE_TEXT)))
        # act_text = self.driver.find_element(By.XPATH, self.CONTACT_NEW_MESSAGE_TEXT)
        # print(act_text)

    def set_all_the_fields(self, contact_email_text, contact_name_text, contact_message_text):
        self.driver.find_element(By.XPATH, self.CONTACT_BUTTON).click()
        self.driver.find_element(By.XPATH, self.CONTACT_EMAIL_TEXT).clear()
        self.driver.find_element(By.XPATH, self.CONTACT_EMAIL_TEXT).send_keys(contact_email_text)
        self.driver.find_element(By.XPATH, self.CONTACT_NAME_TEXT).clear()
        self.driver.find_element(By.XPATH, self.CONTACT_NAME_TEXT).send_keys(contact_name_text)
        self.driver.find_element(By.XPATH, self.CONTACT_MESSAGE_TEXT).clear()
        self.driver.find_element(By.XPATH, self.CONTACT_MESSAGE_TEXT).send_keys(contact_message_text)
        self.driver.find_element(By.XPATH, self.CONTACT_SEND_MESSAGE_BUTTON).click()

    def click_on_contact_close_button(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.CONTACT_CLOSE_BUTTON)))
        self.driver.find_element(By.XPATH, self.CONTACT_BUTTON).click()
        self.driver.find_element(By.XPATH, self.CONTACT_CLOSE_BUTTON).click()

    def click_on_contact_x_mark(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.CONTACT_X_MARK)))
        self.driver.find_element(By.XPATH, self.CONTACT_BUTTON).click()
        self.driver.find_element(By.XPATH, self.CONTACT_X_MARK).click()
