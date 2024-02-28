import allure
import pytest
import time

from allure_commons.types import AttachmentType
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.custom_Logger import Log_Generator
from pageObjects.Home_Page import Home_page
from utilities.readProperties import ReadConfig


@allure.description("validate_home_page")
@allure.severity(allure.severity_level.CRITICAL)
class TestCase002HomePage:

    data = ReadConfig.get_json_data()
    try:
        HOME_BUTTON = data["Home_Page"]["HOME_BUTTON"]
    except Exception as e:
        print(f"{e}: No such element found in json file.")

    logger = Log_Generator.log_gen()

    @allure.description("validate_homepage_button")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_case_001_validate_homepage_button(self, setup_and_teardown):
        self.logger.info("-----test_case_001_validate_homepage_button-----")
        self.logger.info("-----Verifying Home Page-----")
        self.driver = setup_and_teardown
        self.hm_page = Home_page(self.driver)
        self.hm_page.click_on_home_page_button()
        actual_title = self.driver.title
        expected_title = 'STORE'
        print(actual_title)
        try:
            if actual_title == expected_title:
                self.logger.info("-----Test case 001 Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\Screenshots\\" + "test_case_001_Home_page.png")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_001_Home_page",
                              attachment_type=AttachmentType.PNG)
                self.logger.error("-----test case 001 is Failed-----")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_001_Home_page.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_case_001_Home_page",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("-----test case 001 is Failed------")
            assert False

    @allure.description("validate_homepage_logo_button")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_case_002_validate_homepage_logo_button(self, setup_and_teardown):
        self.logger.info("-----test_case_002_validate_homepage_logo_button-----")
        self.logger.info("-----Verifying Home Page-----")
        self.driver = setup_and_teardown
        self.hm_page = Home_page(self.driver)
        self.hm_page.click_on_home_page_logo()
        actual_title = self.driver.title
        expected_title = 'STORE'
        print(actual_title)
        try:
            if actual_title == expected_title:
                self.logger.info("-----Test case 002 Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\Screenshots\\" + "test_case_002_Home_page.png")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_002_Home_page",
                              attachment_type=AttachmentType.PNG)
                self.logger.error("-----test case 002 is Failed-----")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_002_Home_page.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_case_002_Home_page",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("-----test case 002 is Failed------")
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_case_003_validate_next_and_previous_slide_buttons_in_homepage(self, setup_and_teardown):
        self.logger.info("-----test_case_003_validate_next_and_previous_slide_buttons_in_homepage-----")
        self.logger.info("-----Verifying Home Page-----")
        self.driver = setup_and_teardown
        self.hm_page = Home_page(self.driver)
        self.hm_page.click_on_next_and_previous_slide_buttons()
        actual_title = self.driver.title
        expected_title = 'STORE'
        print(actual_title)
        try:
            WebDriverWait(self.driver, 10).until(EC.title_is('STORE'))
            if actual_title == expected_title:
                self.logger.info("-----Test case 003 Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\Screenshots\\" + "test_case_003_Home_page.png")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_003_Home_page",
                              attachment_type=AttachmentType.PNG)
                self.logger.error("-----test case 003 is Failed-----")
                assert False
        except (TimeoutException, AssertionError) as e:
            print(e)
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_003_Home_page.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_case_003_Home_page",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("-----test case 003 is Failed------")
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_case_004_validate_next_and_previous_buttons_at_below_the_homepage(self, setup_and_teardown):
        self.logger.info("-----test_case_004_validate_next_and_previous_buttons_at_below_the_homepage-----")
        self.logger.info("-----Verifying Home Page-----")
        self.driver = setup_and_teardown
        self.hm_page = Home_page(self.driver)
        self.hm_page.click_on_home_page_next_and_previous_button()
        actual_title = self.driver.title
        expected_title = 'STORE'
        print(actual_title)
        try:
            if actual_title == expected_title:
                self.logger.info("-----Test case 004 Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\Screenshots\\" + "test_case_004_Home_page.png")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_004_Home_page",
                              attachment_type=AttachmentType.PNG)
                self.logger.error("-----test case 004 is Failed-----")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_004_Home_page.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_case_004_Home_page",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("-----test case 004 is Failed------")
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_005_validate_categories_button_in_homepage(self, setup_and_teardown):
        self.logger.info("-----test_case_005_validate_categories_button_in_homepage-----")
        self.logger.info("-----Verifying Home Page-----")
        self.driver = setup_and_teardown
        self.hm_page = Home_page(self.driver)
        self.hm_page.click_on_categories_button()
        actual_title = self.driver.title
        expected_title = 'STORE'
        print(actual_title)
        try:
            if actual_title == expected_title:
                self.logger.info("-----Test case 005 Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\Screenshots\\" + "test_case_005_Home_page.png")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_005_Home_page",
                              attachment_type=AttachmentType.PNG)
                self.logger.error("-----test case 005 is Failed-----")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_005_Home_page.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_case_005_Home_page",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("-----test case 005 is Failed------")
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_006_validate_phones_in_categories_button_at_homepage(self, setup_and_teardown):
        self.logger.info("-----test_case_006_validate_phones_in_categories_button_at_homepage-----")
        self.logger.info("-----Verifying Home Page-----")
        self.driver = setup_and_teardown
        self.hm_page = Home_page(self.driver)
        self.hm_page.click_on_phones_button_from_categories()
        actual_title = self.driver.title
        expected_title = 'STORE'
        print(actual_title)
        try:
            if actual_title == expected_title:
                self.logger.info("-----Test case 006 Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\Screenshots\\" + "test_case_006_Home_page.png")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_006_Home_page",
                              attachment_type=AttachmentType.PNG)
                self.logger.error("-----test case 006 is Failed-----")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_006_Home_page.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_case_006_Home_page",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("-----test case 006 is Failed------")
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_007_validate_Laptops_in_categories_button_at_homepage(self, setup_and_teardown):
        self.logger.info("-----test_case_007_validate_Laptops_in_categories_button_at_homepage-----")
        self.logger.info("-----Verifying Home Page-----")
        self.driver = setup_and_teardown
        self.hm_page = Home_page(self.driver)
        self.hm_page.click_on_Laptops_button_from_categories()
        actual_title = self.driver.title
        expected_title = 'STORE'
        print(actual_title)
        try:
            if actual_title == expected_title:
                self.logger.info("-----Test case 007 Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\Screenshots\\" + "test_case_007_Home_page.png")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_007_Home_page",
                              attachment_type=AttachmentType.PNG)
                self.logger.error("-----test case 007 is Failed-----")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_007_Home_page.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_case_007_Home_page",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("-----test case 007 is Failed------")
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_008_validate_Monitors_in_categories_button_at_homepage(self, setup_and_teardown):
        self.logger.info("-----test_case_008_validate_Monitors_in_categories_button_at_homepage-----")
        self.logger.info("-----Verifying Home Page-----")
        self.driver = setup_and_teardown
        self.hm_page = Home_page(self.driver)
        self.hm_page.click_on_Monitors_button_from_categories()
        actual_title = self.driver.title
        expected_title = 'STORE'
        print(actual_title)
        try:
            if actual_title == expected_title:
                self.logger.info("-----Test case 008 Passed-----")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\Screenshots\\" + "test_case_008_Home_page.png")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_008_Home_page",
                              attachment_type=AttachmentType.PNG)
                self.logger.error("-----test case 008 is Failed-----")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_008_Home_page.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_case_008_Home_page",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("-----test case 008 is Failed------")
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_009_validate_phones_and_add_to_cart_the_products(self, setup_and_teardown):
        self.logger.info("-----test_case_009_validate_phones_and_add_to_cart_the_products-----")
        self.logger.info("-----Verifying Phones and add to cart-----")
        self.driver = setup_and_teardown
        self.hm_page = Home_page(self.driver)
        self.hm_page.Add_Samsung_galaxy_s6()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()
        expected_message = "Product added"
        lst_result = []
        try:
            if actual_message == expected_message:
                self.logger.info("-----Samsung_galaxy_s6 added-----")
                lst_result.append('pass')
            else:
                time.sleep(5)
                self.logger.error("-----Samsung_galaxy_s6 not added-----")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_009_Samsung_galaxy_s6",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_009_Samsung_galaxy_s6.png")
                lst_result.append('fail')
        except Exception as e:
            print(e)
            self.logger.error("-----Samsung_galaxy_s6 Page not displayed-----")

        self.hm_page.Add_Nokia_lumia_1520()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()
        expected_message = "Product added"
        try:
            if actual_message == expected_message:
                self.logger.info("-----Nokia_lumia_1520 added-----")
                lst_result.append('pass')
            else:
                time.sleep(5)
                self.logger.error("-----Nokia_lumia_1520 not added-----")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_009_Nokia_lumia_1520",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_009_Nokia_lumia_1520.png")
                lst_result.append('fail')
        except Exception as e:
            print(e)
            self.logger.error("-----Nokia_lumia_1520 Page not displayed-----")

        self.hm_page.Add_Nexus_6()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()
        expected_message = "Product added"
        try:
            if actual_message == expected_message:
                self.logger.info("-----Nexus_6 added-----")
                lst_result.append('pass')
            else:
                time.sleep(5)
                self.logger.error("-----Nexus_6 not added-----")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_009_Nexus_6",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_009_Nexus_6.png")
                lst_result.append('fail')
        except Exception as e:
            print(e)
            self.logger.error("-----Nexus_6 Page not displayed-----")

        self.hm_page.Add_Samsung_galaxy_s7()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()
        expected_message = "Product added"
        try:
            if actual_message == expected_message:
                self.logger.info("-----Samsung_galaxy_s7 added-----")
                lst_result.append('pass')
            else:
                time.sleep(5)
                self.logger.error("-----Samsung_galaxy_s7 not added-----")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_009_Samsung_galaxy_s7",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_009_Samsung_galaxy_s7.png")
                lst_result.append('fail')
        except Exception as e:
            print(e)
            self.logger.error("-----Samsung_galaxy_s7 Page not displayed-----")

        self.hm_page.Add_Iphone_6_32_gb()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()
        expected_message = "Product added"
        try:
            if actual_message == expected_message:
                self.logger.info("-----Iphone_6_32_gb added-----")
                lst_result.append('pass')
            else:
                time.sleep(5)
                self.logger.error("-----Iphone_6_32_gb not added-----")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_009_Iphone_6_32_gb",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_009_Iphone_6_32_gb.png")
                lst_result.append('fail')
        except Exception as e:
            print(e)
            self.logger.error("-----Iphone_6_32_gb Page not displayed-----")

        self.hm_page.Add_Sony_xperia_z5()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()
        expected_message = "Product added"
        try:
            if actual_message == expected_message:
                self.logger.info("-----Sony_xperia_z5 added-----")
                lst_result.append('pass')
            else:
                time.sleep(5)
                self.logger.error("----Sony_xperia_z5 not added-----")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_009_Sony_xperia_z5",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_009_Sony_xperia_z5.png")
                lst_result.append('fail')
        except Exception as e:
            print(e)
            self.logger.error("-----Sony_xperia_z5 Page not displayed-----")

        self.hm_page.Add_HTC_One_M9()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()
        expected_message = "Product added"
        try:
            if actual_message == expected_message:
                self.logger.info("-----HTC_One_M9 added-----")
                lst_result.append('pass')
            else:
                time.sleep(5)
                self.logger.error("-----HTC_One_M9 not added-----")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_009_HTC_One_M9",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_009_HTC_One_M9.png")
                lst_result.append('fail')
        except Exception as e:
            print(e)
            self.logger.error("-----HTC_One_M9 Page not displayed-----")

        try:
            if 'fail' not in lst_result:
                self.logger.info("-----Phones add to cart test case 009 is Passed-----")
                assert True
            else:
                self.logger.error("-----Phones add to cart test case 009 is Failed-----")
                assert False
        except TimeoutException:
            self.logger.error("-----Phones add to cart Test case 009 is not executed(Failed)-----")

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_010_validate_Laptops_add_to_cart_the_products(self, setup_and_teardown):
        self.logger.info("-----test_case_010_validate_Laptops_add_to_cart_the_products-----")
        self.logger.info("-----Verifying Laptops in Home page-----")
        self.driver = setup_and_teardown
        self.hm_page = Home_page(self.driver)
        self.hm_page.Add_Sony_vaio_i5()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()
        expected_message = "Product added"
        lst_result = []
        try:
            if actual_message == expected_message:
                self.logger.info("-----Sony_vaio_i5 added-----")
                lst_result.append('pass')
            else:
                time.sleep(5)
                self.logger.error("-----Sony_vaio_i5 not added-----")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_010_Sony_vaio_i5",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_010_Sony_vaio_i5.png")
                lst_result.append('fail')
        except Exception as e:
            print(e)
            self.logger.error("-----Sony_vaio_i5 Page not displayed-----")

        self.hm_page.Add_Sony_vaio_i7()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()
        expected_message = "Product added"
        try:
            if actual_message == expected_message:
                self.logger.info("-----Sony_vaio_i7 added-----")
                lst_result.append('pass')
            else:
                time.sleep(5)
                self.logger.error("-----Sony_vaio_i7 not added-----")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_010_Sony_vaio_i7",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_010_Sony_vaio_i7.png")
                lst_result.append('fail')
        except Exception as e:
            print(e)
            self.logger.error("-----Sony_vaio_i7 Page not displayed-----")

        self.hm_page.Add_MacBook_air()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()
        expected_message = "Product added"
        try:
            if actual_message == expected_message:
                self.logger.info("-----MacBook_air added-----")
                lst_result.append('pass')
            else:
                time.sleep(5)
                self.logger.error("-----MacBook_air not added-----")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_010_MacBook_air",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_010_MacBook_air.png")
                lst_result.append('fail')

        except Exception as e:
            print(e)
            self.logger.error("-----MacBook_air Page not displayed-----")

        self.hm_page.Add_Dell_i7_8_gb()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()
        expected_message = "Product added"
        try:
            if actual_message == expected_message:
                self.logger.info("-----Dell_i7_8_gb added-----")
                lst_result.append('pass')
            else:
                time.sleep(5)
                self.logger.error("-----Dell_i7_8_gb not added-----")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_010_Dell_i7_8_gb",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_010_Dell_i7_8_gb.png")
                lst_result.append('fail')
        except Exception as e:
            print(e)
            self.logger.error("-----Dell_i7_8_gb Page not displayed-----")

        self.hm_page.Add_2017_Dell_15_6_Inch()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()
        expected_message = "Product added"
        try:
            if actual_message == expected_message:
                self.logger.info("-----2017_Dell_15_6_Inch added-----")
                lst_result.append('pass')
            else:
                time.sleep(5)
                self.logger.error("-----2017_Dell_15_6_Inch not added-----")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_010_2017_Dell_15_6_Inch",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_010_2017_Dell_15_6_Inch.png")
                lst_result.append('fail')
        except Exception as e:
            print(e)
            self.logger.error("-----2017_Dell_15_6_Inch Page not displayed-----")

        self.hm_page.Add_MacBook_Pro()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()
        expected_message = "Product added"
        try:
            if actual_message == expected_message:
                self.logger.info("-----MacBook_Pro added-----")
                lst_result.append('pass')
            else:
                time.sleep(5)
                self.logger.error("-----MacBook_Pro not added-----")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_010_MacBook_Pro",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_010_MacBook_Pro.png")
                lst_result.append('fail')
        except Exception as e:
            print(e)
            self.logger.error("-----MacBook_Pro Page not displayed-----")

        try:
            if 'fail' not in lst_result:
                self.logger.info("-----Laptops add to cart test case 010 is Passed-----")
                assert True
            else:
                self.logger.error("-----Laptops add to cart test case 010 is Failed-----")
                assert False
        except TimeoutException:
            self.logger.error("-----Laptops add to cart Test case 010 not executed(Failed)-----")

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_case_011_validate_monitors_add_to_cart_the_products(self, setup_and_teardown):
        self.logger.info("-----test_case_011_validate_monitors_add_to_cart_the_products-----")
        self.logger.info("-----Verifying Laptops in Home page-----")
        self.driver = setup_and_teardown
        self.hm_page = Home_page(self.driver)
        self.hm_page.Add_Apple_monitor_24()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()
        expected_message = "Product added"
        lst_result = []
        try:
            if actual_message == expected_message:
                self.logger.info("-----Apple_monitor_24 added-----")
                lst_result.append('pass')
            else:
                time.sleep(5)
                self.logger.error("-----Apple_monitor_24 not added-----")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_011_Apple_monitor_24",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_011_Apple_monitor_24.png")
                lst_result.append('fail')
        except Exception as e:
            print(e)
            self.logger.error("-----Apple_monitor_24 Page not displayed-----")

        self.hm_page.Add_ASUS_Full_HD()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()
        expected_message = "Product added"
        lst_result = []
        try:
            if actual_message == expected_message:
                self.logger.info("-----ASUS_Full_HD added-----")
                lst_result.append('pass')
            else:
                time.sleep(5)
                self.logger.error("-----ASUS_Full_HD not added-----")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_case_011_ASUS_Full_HD",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_case_011_ASUS_Full_HD.png")
                lst_result.append('fail')
        except Exception as e:
            print(e)
            self.logger.error("-----ASUS_Full_HD Page not displayed-----")

        try:
            if 'fail' not in lst_result:
                self.logger.info("-----Monitors add to cart test case 011 is Passed-----")
                assert True
            else:
                self.logger.error("-----Monitors add to cart test case 011 is Failed-----")
                assert False
        except TimeoutException:
            self.logger.error("-----Monitors add to cart Test case 011 is not executed(Failed)-----")
