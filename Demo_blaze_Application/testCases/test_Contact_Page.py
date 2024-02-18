# import pytest
# from selenium.webdriver import Chrome
import time

import pytest
from selenium.common import TimeoutException
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
    Contact_page_text = "//*[@id='exampleModalLabel']"

    logger = Log_Generator.log_gen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_001_validate_contact_with_valid_email_valid_name_valid_message(self, setup_and_teardown):
        self.logger.info("-----test_case_001_validate_contact_with_valid_email_valid_name_valid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.valid_email, self.valid_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text == "Thanks for the message!!":
                self.logger.info("-----test case 001 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.logger.error("-----test case 001 is Failed-----")
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_001_contact.png")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_001_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_002_validate_contact_with_valid_email_valid_name_invalid_message(self, setup_and_teardown):
        self.logger.info("-----test_case_002_validate_contact_with_valid_email_valid_name_invalid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.valid_email, self.valid_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 002 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_002_contact.png")
                self.logger.error("-----test case 002 is Failed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_002_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_003_validate_contact_with_valid_email_valid_name_no_message(self, setup_and_teardown):
        self.logger.info("-----test_case_003_validate_contact_with_valid_email_valid_name_no_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.valid_email, self.valid_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 003 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_003_contact.png")
                self.logger.error("-----test case 003 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_003_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_004_validate_contact_with_valid_email_invalid_name_valid_message(self, setup_and_teardown):
        self.logger.info("-----test_case_004_validate_contact_with_valid_email_invalid_name_valid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.valid_email, self.invalid_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 004 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_004_contact.png")
                self.logger.error("-----test case 004 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_004_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_005_validate_contact_with_valid_email_invalid_name_invalid_message(self, setup_and_teardown):
        self.logger.info("-----test_case_005_validate_contact_with_valid_email_invalid_name_invalid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.valid_email, self.invalid_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 005 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_005_contact.png")
                self.logger.error("-----test case 005 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_005_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_006_validate_contact_with_valid_email_invalid_name_no_message(self, setup_and_teardown):
        self.logger.info("-----test_case_006_validate_contact_with_valid_email_invalid_name_no_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.valid_email, self.invalid_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 006 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_006_contact.png")
                self.logger.error("-----test case 006 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_006_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_007_validate_contact_with_valid_email_no_name_valid_message(self, setup_and_teardown):
        self.logger.info("-----test_case_007_validate_contact_with_valid_email_no_name_valid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.valid_email, self.no_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 007 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_007_contact.png")
                self.logger.error("-----test case 007 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_007_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_008_validate_contact_with_valid_email_no_name_invalid_message(self, setup_and_teardown):
        self.logger.info("-----test_case_008_validate_contact_with_valid_email_no_name_invalid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.valid_email, self.no_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 008 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_008_contact.png")
                self.logger.error("-----test case 008 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_008_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_009_validate_contact_with_valid_email_no_name_no_message(self, setup_and_teardown):
        self.logger.info("-----test_case_009_validate_contact_with_valid_email_no_name_no_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.valid_email, self.no_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 009 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_009_contact.png")
                self.logger.error("-----test case 009 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_009_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_010_validate_contact_with_invalid_email_valid_name_valid_message(self, setup_and_teardown):
        self.logger.info("-----test_case_010_validate_contact_with_invalid_email_valid_name_valid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.invalid_email, self.valid_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 010 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_010_contact.png")
                self.logger.error("-----test case 010 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_010_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_011_validate_contact_with_invalid_email_valid_name_invalid_message(self, setup_and_teardown):
        self.logger.info("-----test_case_011_validate_contact_with_invalid_email_valid_name_invalid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.invalid_email, self.valid_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 011 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_011_contact.png")
                self.logger.error("-----test case 011 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_011_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_012_validate_contact_with_invalid_email_valid_name_no_message(self, setup_and_teardown):
        self.logger.info("-----test_case_012_validate_contact_with_invalid_email_valid_name_no_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.invalid_email, self.valid_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 012 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_012_contact.png")
                self.logger.error("-----test case 012 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_012_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_013_validate_contact_with_invalid_email_invalid_name_valid_message(self, setup_and_teardown):
        self.logger.info("-----test_case_013_validate_contact_with_invalid_email_invalid_name_valid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.invalid_email, self.invalid_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 013 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_013_contact.png")
                self.logger.error("-----test case 013 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_013_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_014_validate_contact_with_invalid_email_invalid_name_invalid_message(self, setup_and_teardown):
        self.logger.info("-----test_case_014_validate_contact_with_invalid_email_invalid_name_invalid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.invalid_email, self.invalid_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 013 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_013_contact.png")
                self.logger.error("-----test case 013 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_013_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_015_validate_contact_with_invalid_email_invalid_name_no_message(self, setup_and_teardown):
        self.logger.info("-----test_case_015_validate_contact_with_invalid_email_invalid_name_no_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.invalid_email, self.invalid_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 015 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_015_contact.png")
                self.logger.error("-----test case 015 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_015_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_016_validate_contact_with_invalid_email_no_name_valid_message(self, setup_and_teardown):
        self.logger.info("-----test_case_016_validate_contact_with_invalid_email_no_name_valid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.invalid_email, self.no_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 016 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_016_contact.png")
                self.logger.error("-----test case 016 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_016_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_017_validate_contact_with_invalid_email_no_name_invalid_message(self, setup_and_teardown):
        self.logger.info("-----test_case_017_validate_contact_with_invalid_email_no_name_invalid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.invalid_email, self.no_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 017 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_017_contact.png")
                self.logger.error("-----test case 017 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_017_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_018_validate_contact_with_invalid_email_no_name_no_message(self, setup_and_teardown):
        self.logger.info("-----test_case_018_validate_contact_with_invalid_email_no_name_no_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.invalid_email, self.no_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 018 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_018_contact.png")
                self.logger.error("-----test case 018 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_018_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_019_validate_contact_with_email_with_spl_chars_valid_name_valid_message(self, setup_and_teardown):
        self.logger.info("-----test_case_019_validate_contact_with_email_with_spl_chars_valid_name_valid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.email_with_spl_chars, self.valid_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 019 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_019_contact.png")
                self.logger.error("-----test case 019 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_019_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_020_validate_contact_with_email_with_spl_chars_valid_name_invalid_message(self, setup_and_teardown):
        self.logger.info(
            "-----test_case_020_validate_contact_with_email_with_spl_chars_valid_name_invalid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.email_with_spl_chars, self.valid_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 020 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_020_contact.png")
                self.logger.error("-----test case 020 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_020_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_021_validate_contact_with_email_with_spl_chars_valid_name_no_message(self, setup_and_teardown):
        self.logger.info("-----test_case_021_validate_contact_with_email_with_spl_chars_valid_name_no_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.email_with_spl_chars, self.valid_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 021 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_021_contact.png")
                self.logger.error("-----test case 021 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_021_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_022_validate_contact_with_email_with_spl_chars_invalid_name_valid_message(self, setup_and_teardown):
        self.logger.info(
            "-----test_case_022_validate_contact_with_email_with_spl_chars_invalid_name_valid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.email_with_spl_chars, self.invalid_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 022 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_022_contact.png")
                self.logger.error("-----test case 022 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_022_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_023_validate_contact_with_email_with_spl_chars_invalid_name_invalid_message(self, setup_and_teardown):
        self.logger.info(
            "-----test_case_023_validate_contact_with_email_with_spl_chars_invalid_name_invalid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.email_with_spl_chars, self.invalid_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 023 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_023_contact.png")
                self.logger.error("-----test case 023 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_023_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_024_validate_contact_with_email_with_spl_chars_invalid_name_no_message(self, setup_and_teardown):
        self.logger.info("-----test_case_024_validate_contact_with_email_with_spl_chars_invalid_name_no_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.email_with_spl_chars, self.invalid_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 024 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_024_contact.png")
                self.logger.error("-----test case 024 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_024_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_025_validate_contact_with_email_with_spl_chars_no_name_valid_message(self, setup_and_teardown):
        self.logger.info("-----test_case_025_validate_contact_with_email_with_spl_chars_no_name_valid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.email_with_spl_chars, self.no_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 025 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_025_contact.png")
                self.logger.error("-----test case 025 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_025_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_026_validate_contact_with_email_with_spl_chars_no_name_invalid_message(self, setup_and_teardown):
        self.logger.info("-----test_case_026_validate_contact_with_email_with_spl_chars_no_name_invalid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.email_with_spl_chars, self.no_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 026 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_026_contact.png")
                self.logger.error("-----test case 026 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_026_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_027_validate_contact_with_email_with_spl_chars_no_name_no_message(self, setup_and_teardown):
        self.logger.info("-----test_case_027_validate_contact_with_email_with_spl_chars_no_name_no_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.email_with_spl_chars, self.no_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 027 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_027_contact.png")
                self.logger.error("-----test case 027 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_027_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_028_validate_contact_with_no_email_valid_name_valid_message(self, setup_and_teardown):
        self.logger.info("-----test_case_028_validate_contact_with_no_email_valid_name_valid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.no_email, self.valid_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 028 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_028_contact.png")
                self.logger.error("-----test case 028 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_028_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_029_validate_contact_with_no_email_valid_name_invalid_message(self, setup_and_teardown):
        self.logger.info("-----test_case_029_validate_contact_with_no_email_valid_name_invalid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.no_email, self.valid_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 029 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_029_contact.png")
                self.logger.error("-----test case 029 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_029_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_030_validate_contact_with_no_email_valid_name_no_message(self, setup_and_teardown):
        self.logger.info("-----test_case_030_validate_contact_with_no_email_valid_name_no_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.no_email, self.valid_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 030 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_030_contact.png")
                self.logger.error("-----test case 030 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_030_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_031_validate_contact_with_no_email_invalid_name_valid_message(self, setup_and_teardown):
        self.logger.info("-----test_case_031_validate_contact_with_no_email_invalid_name_valid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.no_email, self.invalid_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 031 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_031_contact.png")
                self.logger.error("-----test case 031 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_031_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_032_validate_contact_with_no_email_invalid_name_invalid_message(self, setup_and_teardown):
        self.logger.info("-----test_case_032_validate_contact_with_no_email_invalid_name_invalid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.no_email, self.invalid_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 032 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_032_contact.png")
                self.logger.error("-----test case 032 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_032_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_033_validate_contact_with_no_email_invalid_name_no_message(self, setup_and_teardown):
        self.logger.info("-----test_case_033_validate_contact_with_no_email_invalid_name_no_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.no_email, self.invalid_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 033 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_033_contact.png")
                self.logger.error("-----test case 033 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_033_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_034_validate_contact_with_no_email_no_name_valid_message(self, setup_and_teardown):
        self.logger.info("-----test_case_034_validate_contact_with_no_email_no_name_valid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.no_email, self.no_name, self.valid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 034 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_034_contact.png")
                self.logger.error("-----test case 034 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_034_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_035_validate_contact_with_no_email_no_name_invalid_message(self, setup_and_teardown):
        self.logger.info("-----test_case_035_validate_contact_with_no_email_no_name_invalid_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.no_email, self.no_name, self.invalid_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 035 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_035_contact.png")
                self.logger.error("-----test case 035 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_035_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_036_validate_contact_with_no_email_no_name_no_message(self, setup_and_teardown):
        self.logger.info("-----test_case_036_validate_contact_with_no_email_no_name_no_message-----")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.set_all_the_fields(self.no_email, self.no_name, self.no_message)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        al_msg = self.driver.switch_to.alert
        alert_text = al_msg.text
        self.driver.switch_to.alert.accept()
        print(alert_text)
        try:
            if alert_text != "Thanks for the message!!":
                self.logger.info("-----test case 036 is Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_036_contact.png")
                self.logger.error("-----test case 036 is Passed-----")
                assert False
        except TimeoutException:
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_036_contact.png")
            self.logger.error("-----Timeout Exception Occurred and Contact page Failed-----")

    @pytest.mark.regression
    def test_case_037_click_on_contact_button(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.click_on_contact_button()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.Contact_page_text)))
        is_displayed = self.driver.find_element(By.XPATH, self.Contact_page_text).is_displayed()
        try:
            if is_displayed:
                actual_text = self.driver.find_element(By.XPATH, self.Contact_page_text).text
                expected_text = "Sign up"
                if actual_text == expected_text:
                    self.logger.info("-----test case 037 is Passed------")
                    assert True
                else:
                    time.sleep(5)
                    self.logger.error("------test case 037 is Failed-----")
                    self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_037_contact.png")
                    assert False
            else:
                time.sleep(5)
                self.logger.error("------Contact title text not Displayed-----")
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_037_contact.png")
                assert False
        except TimeoutException:
            self.logger.error("-----TimeoutException: Contact page not displayed------")
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_037.png")

    @pytest.mark.regression
    def test_case_038_click_on_contact_close_button(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.click_on_contact_close_button()
        act_title = self.driver.title
        try:
            if act_title == "STORE":
                self.logger.info("-----test case 038 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.logger.error("------test case 038 is Failed-----")
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_038_contact.png")
                assert False
        except TimeoutException:
            self.logger.error("-----TimeoutException: Contact page not displayed------")
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_037_timeout.png")

    @pytest.mark.regression
    def test_case_039_click_on_contact_x_mark(self, setup_and_teardown):
        self.logger.info("")
        self.logger.info("-----Verifying Contact Page-----")
        self.driver = setup_and_teardown
        self.cnt_page = Contact_page(self.driver)
        self.cnt_page.click_on_contact_x_mark()
        act_title = self.driver.title
        try:
            if act_title == "STORE":
                self.logger.info("-----test case 039 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.logger.error("------test case 039 is Failed-----")
                self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_039_contact.png")
                assert False
        except TimeoutException:
            self.logger.error("-----TimeoutException: Contact page not displayed------")
            self.driver.save_screenshot(".\\ScreenShots\\Contact_Page\\" + "test_case_039_timeout.png")
