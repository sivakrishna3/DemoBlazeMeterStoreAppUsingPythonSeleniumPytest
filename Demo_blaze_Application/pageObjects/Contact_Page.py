# import pytest
# from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Contact_page:
    CONTACT_BUTTON = "//a[@class = 'nav-link' and contains(text(),'Contact')]"
    CONTACT_EMAIL_TEXT = "//*[@id='recipient-email']"
    CONTACT_NAME_TEXT = "//*[@id='recipient-name']"
    CONTACT_MESSAGE_TEXT = "//*[@id='message-text']"
    CONTACT_SEND_MESSAGE_BUTTON = ("//button[contains(text(),'Send message') and //*["
                                   "@id='exampleModal']/div/div/div/button]")
    CONTACT_CLOSE_BUTTON = "//*[@id='exampleModal' and //button[contains(text(),'Close')]]/div/div/div[3]/button[1]"
    CONTACT_X_MARK = "//*[@id='exampleModal']/div/div/div[1]/button"
    CONTACT_NEW_MESSAGE_TEXT = "//*[@id='exampleModalLabel']"

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

    # def set_contact_email_data(self, contact_email_text):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.CONTACT_EMAIL_TEXT)))
    #     self.driver.find_element(By.XPATH, self.CONTACT_EMAIL_TEXT).clear()
    #     self.driver.find_element(By.XPATH, self.CONTACT_EMAIL_TEXT).send_keys(contact_email_text)

    # def set_contact_name_text(self, contact_name_text):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.CONTACT_NAME_TEXT)))
    #     self.driver.find_element(By.XPATH, self.CONTACT_NAME_TEXT).clear()
    #     self.driver.find_element(By.XPATH, self.CONTACT_NAME_TEXT).send_keys(contact_name_text)

    # def set_contact_message_text(self, contact_message_text):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.CONTACT_MESSAGE_TEXT)))
    #     self.driver.find_element(By.XPATH, self.CONTACT_MESSAGE_TEXT).clear()
    #     self.driver.find_element(By.XPATH, self.CONTACT_MESSAGE_TEXT).send_keys(contact_message_text)

    # def click_on_contact_send_message_button(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(
    #         EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.CONTACT_SEND_MESSAGE_BUTTON)))
    #     self.driver.find_element(By.XPATH, self.CONTACT_SEND_MESSAGE_BUTTON).click()

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
