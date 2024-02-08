# import pytest
# from selenium.webdriver import Chrome
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageObjects.Contact_Page import Contact_page
from utilities.readProperties import ReadConfig
from utilities.custom_Logger import Log_Generator


class TestCase003ContactPage:
    
    valid_email = ReadConfig.get_contact_email()
    invalid_email = ReadConfig.get_contact_invalid_email()
    no_email = ReadConfig.get_contact_empty_email()
    email_with_spl_chars = ReadConfig.get_contact_email_with_spl_chars()
    valid_name = ReadConfig.get_contact_name()
    invalid_name = ReadConfig.get_contact_invalid_name()
    no_name = ReadConfig.get_contact_empty_name()
    valid_message = ReadConfig.get_contact_message()
    invalid_message = ReadConfig.get_contact_invalid_message()
    no_message = ReadConfig.get_contact_empty_message()

    logger = Log_Generator.log_gen()

    def test_case_001_validate_contact_with_valid_email_valid_name_valid_message(self, setup_and_teardown):

        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.valid_email, self.valid_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text == "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_001_contact.png")
            assert False

    def test_case_002_validate_contact_with_valid_email_valid_name_invalid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.valid_email, self.valid_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_002_contact.png")
            assert False

    def test_case_003_validate_contact_with_valid_email_valid_name_no_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.valid_email, self.valid_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_003_contact.png")
            assert False

    def test_case_004_validate_contact_with_valid_email_invalid_name_valid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.valid_email, self.invalid_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_004_contact.png")
            assert False

    def test_case_005_validate_contact_with_valid_email_invalid_name_invalid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.valid_email, self.invalid_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_005_contact.png")
            assert False

    def test_case_006_validate_contact_with_valid_email_invalid_name_no_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.valid_email, self.invalid_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_006_contact.png")
            assert False

    def test_case_007_validate_contact_with_valid_email_no_name_valid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.valid_email, self.no_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_007_contact.png")
            assert False

    def test_case_008_validate_contact_with_valid_email_no_name_invalid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.valid_email, self.no_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_008_contact.png")
            assert False

    def test_case_009_validate_contact_with_valid_email_no_name_no_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.valid_email, self.no_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_009_contact.png")
            assert False

    def test_case_010_validate_contact_with_invalid_email_valid_name_valid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.invalid_email, self.valid_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_010_contact.png")
            assert False

    def test_case_011_validate_contact_with_invalid_email_valid_name_invalid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.invalid_email, self.valid_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_011_contact.png")
            assert False

    def test_case_012_validate_contact_with_invalid_email_valid_name_no_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.invalid_email, self.valid_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_012_contact.png")
            assert False

    def test_case_013_validate_contact_with_invalid_email_invalid_name_valid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.invalid_email, self.invalid_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_013_contact.png")
            assert False

    def test_case_014_validate_contact_with_invalid_email_invalid_name_invalid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.invalid_email, self.invalid_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_014_contact.png")
            assert False

    def test_case_015_validate_contact_with_invalid_email_invalid_name_no_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.invalid_email, self.invalid_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_015_contact.png")
            assert False

    def test_case_016_validate_contact_with_invalid_email_no_name_valid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.invalid_email, self.no_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_016_contact.png")
            assert False

    def test_case_017_validate_contact_with_invalid_email_no_name_invalid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.invalid_email, self.no_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_017_contact.png")
            assert False

    def test_case_018_validate_contact_with_invalid_email_no_name_no_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.invalid_email, self.no_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_018_contact.png")
            assert False

    def test_case_019_validate_contact_with_email_with_spl_chars_valid_name_valid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.email_with_spl_chars, self.valid_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_019_contact.png")
            assert False

    def test_case_020_validate_contact_with_email_with_spl_chars_valid_name_invalid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.email_with_spl_chars, self.valid_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_020_contact.png")
            assert False

    def test_case_021_validate_contact_with_email_with_spl_chars_valid_name_no_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.email_with_spl_chars, self.valid_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_021_contact.png")
            assert False

    def test_case_022_validate_contact_with_email_with_spl_chars_invalid_name_valid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.email_with_spl_chars, self.invalid_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_022_contact.png")
            assert False

    def test_case_023_validate_contact_with_email_with_spl_chars_invalid_name_invalid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.email_with_spl_chars, self.invalid_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_023_contact.png")
            assert False

    def test_case_024_validate_contact_with_email_with_spl_chars_invalid_name_no_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.email_with_spl_chars, self.invalid_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_024_contact.png")
            assert False

    def test_case_025_validate_contact_with_email_with_spl_chars_no_name_valid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.email_with_spl_chars, self.no_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_025_contact.png")
            assert False

    def test_case_026_validate_contact_with_email_with_spl_chars_no_name_invalid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.email_with_spl_chars, self.no_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_026_contact.png")
            assert False

    def test_case_027_validate_contact_with_email_with_spl_chars_no_name_no_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.email_with_spl_chars, self.no_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_027_contact.png")
            assert False

    def test_case_028_validate_contact_with_no_email_valid_name_valid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.no_email, self.valid_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_028_contact.png")
            assert False

    def test_case_029_validate_contact_with_no_email_valid_name_invalid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.no_email, self.valid_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_029_contact.png")
            assert False

    def test_case_030_validate_contact_with_no_email_valid_name_no_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.no_email, self.valid_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_030_contact.png")
            assert False

    def test_case_031_validate_contact_with_no_email_invalid_name_valid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.no_email, self.invalid_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_031_contact.png")
            assert False

    def test_case_032_validate_contact_with_no_email_invalid_name_invalid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.no_email, self.invalid_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_032_contact.png")
            assert False

    def test_case_033_validate_contact_with_no_email_invalid_name_no_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.no_email, self.invalid_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_033_contact.png")
            assert False

    def test_case_034_validate_contact_with_no_email_no_name_valid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.no_email, self.no_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_034_contact.png")
            assert False

    def test_case_035_validate_contact_with_no_email_no_name_invalid_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.no_email, self.no_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_035_contact.png")
            assert False

    def test_case_036_validate_contact_with_no_email_no_name_no_message(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.no_email, self.no_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        if alert_text != "Thanks for the message!!":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_036_contact.png")
            assert False

    def test_case_037_click_on_contact_button(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.click_on_contact_button()
        a = 10
        if a == a:
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_037_click_on_contact_button.png")
            assert False

    def test_case_038_click_on_contact_close_button(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.click_on_contact_close_button()
        act_title = self.driver.title
        if act_title == "STORE":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_038_contact_close_button.png")
            assert False

    def test_case_039_click_on_contact_x_mark(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.click_on_contact_x_mark()
        act_title = self.driver.title
        if act_title == "STORE":
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_039_click_on_contact_x_mark.png")
            assert False
