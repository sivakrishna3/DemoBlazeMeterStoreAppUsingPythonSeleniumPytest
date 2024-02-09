import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.custom_Logger import Log_Generator
from pageObjects.Cart_Page import Cart_page
from utilities.readProperties import ReadConfig


class TestCase005CartPage:

    logger = Log_Generator.log_gen()
    cart_page_text = "//*[@id='page-wrapper']/div/div[1]/h2"
    place_order_text = "//*[@id='orderModalLabel']"
    order_success_message = "/html/body/div[10]/h2"
    order_success_ok_button = "/html/body/div[10]/div[7]/div/button"

    name = ReadConfig.get_cart_name()
    no_name = ReadConfig.get_cart_no_name()
    country = ReadConfig.get_cart_country()
    no_country = ReadConfig.get_cart_no_country()
    city = ReadConfig.get_cart_city()
    no_city = ReadConfig.get_cart_no_city()
    credit_card = ReadConfig.get_cart_credit_card()
    no_credit_card = ReadConfig.get_cart_no_credit_card()
    month = ReadConfig.get_cart_month()
    no_month = ReadConfig.get_cart_no_month()
    year = ReadConfig.get_cart_year()
    no_year = ReadConfig.get_cart_no_year()

    def test_case_001_validate_Cart_button(self, setup_and_teardown):
        self.logger.info("-----test_case_001_validate_Cart_button-----")
        self.logger.info("-----Verifying Cart Page------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.clicking_on_cart_button()
        is_displayed = self.driver.find_element(By.XPATH, self.cart_page_text).is_displayed()
        try:
            if is_displayed:
                actual_text = self.driver.find_element(By.XPATH, self.cart_page_text).text
                expected_text = "Products"

                if actual_text == expected_text:
                    self.logger.info("-----test case 001 is Passed------")
                    assert True
                else:
                    time.sleep(5)
                    self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_001.png")
                    self.logger.error("-----test case 001 is Failed.------")
                    assert False
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_001.png")
                self.logger.error("-----test case 001 is Failed. Cart Page not displayed------")
                assert False
        except Exception as e:
            print(e)
            assert False

    def test_case_002_validate_add_to_cart_button(self, setup_and_teardown):
        self.logger.info("-----test_case_002_validate_add_to_cart_button-----")
        self.logger.info("-------------------Verifying------------------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.adding_product_to_cart()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        exp_message = "Product added"
        try:
            if actual_message == exp_message:
                self.logger.info("-----test case 002 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_002.png")
                self.logger.error("-----test case 002 is Failed------")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_002.png")
            self.logger.error("-----test case 002 is Failed------")
            assert False

    def test_case_003_validate_delete_the_product_button(self, setup_and_teardown):
        self.logger.info("-----test_case_003_validate_delete_the_product_button-----")
        self.logger.info("-------------------Verifying------------------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.clicking_on_delete_option()
        is_displayed = self.driver.find_element(By.XPATH, self.cart_page_text).is_displayed()
        try:
            if is_displayed:
                actual_text = self.driver.find_element(By.XPATH, self.cart_page_text).text
                expected_text = "Products"

                if actual_text == expected_text:
                    self.logger.info("-----test case 003 is Passed------")
                    assert True
                else:
                    time.sleep(5)
                    self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_003.png")
                    self.logger.error("-----test case 003 is Failed.------")
                    assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_003.png")
            self.logger.error("-----test case 003 is Failed. Cart Page not displayed------")
            assert False

    def test_case_004_validate_place_order_button(self, setup_and_teardown):
        self.logger.info("-----test_case_004_validate_place_order_button-----")
        self.logger.info("-----Verifying Place order button-------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.clicking_on_place_order_button()
        try:
            place_order_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.place_order_text)))
            act_message = place_order_element.text
            exp_message = "Place order"

            if act_message == exp_message:
                self.logger.info("-----test case 004 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_004.png")
                self.logger.error("-----test case 004 is Failed. Unexpected Place order button text------")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_004.png")
            self.logger.error("-----test case 004 is Failed. Place order button not displayed------")
            assert False

    def test_case_005_validate_place_order_and_set_all_fields_with_adding_product(self, setup_and_teardown):
        self.logger.info("-----test_case_005_validate_place_order_and_set_all_fields_with_adding_product-----")
        self.logger.info("-------------------Verifying------------------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.click_on_place_order_to_continue_with_product(self.name, self.country, self.city,
                                                                   self.credit_card, self.month, self.year)
        success_message = self.driver.find_element(By.XPATH, self.order_success_message)
        act_message = success_message.text
        exp_message = "Thank you for your purchase!"
        print(act_message)
        try:
            if act_message == exp_message:
                self.logger.info("-----test case 005 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_005.png")
                self.logger.error("-----test case 005 is Failed------")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_005.png")
            self.logger.error("-----test case 005 is Failed------")
            assert False

    def test_case_006_validate_place_order_and_set_all_fields_without_adding_product(self, setup_and_teardown):
        self.logger.info("-----test_case_006_validate_place_order_and_set_all_fields_without_adding_product-----")
        self.logger.info("-------------------Verifying------------------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.click_on_place_order_to_continue_without_product(self.name, self.country, self.city,
                                                                      self.credit_card, self.month, self.year)
        success_message = self.driver.find_element(By.XPATH, self.order_success_message)
        act_message = success_message.text
        exp_message = "Thank you for your purchase!"
        print(act_message)
        try:
            if act_message == exp_message:
                self.logger.info("-----test case 006 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_006.png")
                self.logger.error("-----test case 006 is Failed------")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_006.png")
            self.logger.error("-----test case 006 is Failed------")
            assert False

    def test_case_007_validate_place_order_and_set_no_name_and_with_adding_product(self, setup_and_teardown):
        self.logger.info("-----test_case_007_validate_place_order_and_set_no_name_and_with_adding_product-----")
        self.logger.info("-------------------Verifying------------------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.click_on_place_order_to_continue_with_product(self.no_name, self.country, self.city,
                                                                   self.credit_card, self.month, self.year)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        expected_message = "Please fill out Name and Creditcard."
        try:
            if actual_message == expected_message:
                self.logger.info("-----test case 007 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_007.png")
                self.logger.error("-----test case 007 is Failed------")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_007.png")
            self.logger.error("-----test case 007 is Failed------")
            assert False

    def test_case_008_validate_place_order_and_set_no_name_and_without_adding_product(self, setup_and_teardown):
        self.logger.info("-----test_case_008_validate_place_order_and_set_no_name_and_without_adding_product-----")
        self.logger.info("-------------------Verifying------------------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.click_on_place_order_to_continue_without_product(self.no_name, self.country, self.city,
                                                                      self.credit_card, self.month, self.year)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        expected_message = "Please fill out Name and Creditcard."
        try:
            if actual_message == expected_message:
                self.logger.info("-----test case 008 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_008.png")
                self.logger.error("-----test case 008 is Failed------")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_008.png")
            self.logger.error("-----test case 008 is Failed------")
            assert False

    def test_case_009_validate_place_order_and_set_no_country_and_with_adding_product(self, setup_and_teardown):
        self.logger.info("-----test_case_009_validate_place_order_and_set_no_country_and_with_adding_product-----")
        self.logger.info("-------------------Verifying------------------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.click_on_place_order_to_continue_with_product(self.name, self.no_country, self.city,
                                                                   self.credit_card, self.month, self.year)
        success_message = self.driver.find_element(By.XPATH, self.order_success_message)
        act_message = success_message.text
        exp_message = "Thank you for your purchase!"
        print(act_message)
        try:
            if act_message == exp_message:
                self.logger.info("-----test case 009 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_009.png")
                self.logger.error("-----test case 009 is Failed------")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_009.png")
            self.logger.error("-----test case 009 is Failed------")
            assert False

    def test_case_010_validate_place_order_and_set_no_country_and_without_adding_product(self, setup_and_teardown):
        self.logger.info("-----test_case_010_validate_place_order_and_set_no_country_and_without_adding_product-----")
        self.logger.info("-------------------Verifying------------------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.click_on_place_order_to_continue_without_product(self.name, self.no_country, self.city,
                                                                      self.credit_card, self.month, self.year)
        success_message = self.driver.find_element(By.XPATH, self.order_success_message)
        act_message = success_message.text
        exp_message = "Thank you for your purchase!"
        print(act_message)
        try:
            if act_message == exp_message:
                self.logger.info("-----test case 010 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_010.png")
                self.logger.error("-----test case 010 is Failed------")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_010.png")
            self.logger.error("-----test case 010 is Failed------")
            assert False

    def test_case_011_validate_place_order_and_set_no_city_and_with_adding_product(self, setup_and_teardown):
        self.logger.info("-----test_case_011_validate_place_order_and_set_no_city_and_with_adding_product-----")
        self.logger.info("-------------------Verifying------------------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.click_on_place_order_to_continue_with_product(self.name, self.country, self.no_city,
                                                                   self.credit_card, self.month, self.year)
        success_message = self.driver.find_element(By.XPATH, self.order_success_message)
        act_message = success_message.text
        exp_message = "Thank you for your purchase!"
        print(act_message)
        try:
            if act_message == exp_message:
                self.logger.info("-----test case 011 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_011.png")
                self.logger.error("-----test case 011 is Failed------")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_011.png")
            self.logger.error("-----test case 011 is Failed------")
            assert False

    def test_case_012_validate_place_order_and_set_no_city_and_without_adding_product(self, setup_and_teardown):
        self.logger.info("-----test_case_012_validate_place_order_and_set_no_city_and_without_adding_product-----")
        self.logger.info("-------------------Verifying------------------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.click_on_place_order_to_continue_without_product(self.name, self.country, self.no_city,
                                                                      self.credit_card, self.month, self.year)
        success_message = self.driver.find_element(By.XPATH, self.order_success_message)
        act_message = success_message.text
        exp_message = "Thank you for your purchase!"
        print(act_message)
        try:
            if act_message == exp_message:
                self.logger.info("-----test case 012 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_012.png")
                self.logger.error("-----test case 012 is Failed------")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_012.png")
            self.logger.error("-----test case 012 is Failed------")
            assert False

    def test_case_013_validate_place_order_and_set_no_credit_card_and_with_adding_product(self, setup_and_teardown):
        self.logger.info("-----test_case_013_validate_place_order_and_set_no_credit_card_and_with_adding_product-----")
        self.logger.info("-------------------Verifying------------------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.click_on_place_order_to_continue_with_product(self.name, self.country, self.city,
                                                                   self.no_credit_card, self.month, self.year)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        expected_message = "Please fill out Name and Creditcard."
        try:
            if actual_message == expected_message:
                self.logger.info("-----test case 013 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_013.png")
                self.logger.error("-----test case 013 is Failed------")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_013.png")
            self.logger.error("-----test case 013 is Failed------")
            assert False

    def test_case_014_validate_place_order_and_set_no_credit_card_and_without_adding_product(self, setup_and_teardown):
        self.logger.info("-----test_case_014_validate_place_order_and_set_no_country_and_without_adding_product-----")
        self.logger.info("-------------------Verifying------------------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.click_on_place_order_to_continue_without_product(self.name, self.country, self.city,
                                                                      self.no_credit_card, self.month, self.year)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        expected_message = "Please fill out Name and Creditcard."
        try:
            if actual_message == expected_message:
                self.logger.info("-----test case 014 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_014.png")
                self.logger.error("-----test case 014 is Failed------")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_014.png")
            self.logger.error("-----test case 014 is Failed------")
            assert False

    def test_case_015_validate_place_order_and_set_no_month_and_with_adding_product(self, setup_and_teardown):
        self.logger.info("-----test_case_015_validate_place_order_and_set_no_month_and_with_adding_product-----")
        self.logger.info("-------------------Verifying------------------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.click_on_place_order_to_continue_with_product(self.name, self.country, self.city,
                                                                   self.credit_card, self.no_month, self.year)
        success_message = self.driver.find_element(By.XPATH, self.order_success_message)
        act_message = success_message.text
        exp_message = "Thank you for your purchase!"
        print(act_message)
        try:
            if act_message == exp_message:
                self.logger.info("-----test case 015 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_015.png")
                self.logger.error("-----test case 015 is Failed------")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_015.png")
            self.logger.error("-----test case 015 is Failed------")
            assert False

    def test_case_016_validate_place_order_and_set_no_month_and_without_adding_product(self, setup_and_teardown):
        self.logger.info("-----test_case_016_validate_place_order_and_set_no_month_and_without_adding_product-----")
        self.logger.info("-------------------Verifying------------------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.click_on_place_order_to_continue_without_product(self.name, self.country, self.city,
                                                                      self.credit_card, self.no_month, self.year)
        success_message = self.driver.find_element(By.XPATH, self.order_success_message)
        act_message = success_message.text
        exp_message = "Thank you for your purchase!"
        print(act_message)
        try:
            if act_message == exp_message:
                self.logger.info("-----test case 016 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_016.png")
                self.logger.error("-----test case 016 is Failed------")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_016.png")
            self.logger.error("-----test case 016 is Failed------")
            assert False

    def test_case_017_validate_place_order_and_set_no_year_and_with_adding_product(self, setup_and_teardown):
        self.logger.info("-----test_case_017_validate_place_order_and_set_no_year_and_with_adding_product-----")
        self.logger.info("-------------------Verifying------------------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.click_on_place_order_to_continue_with_product(self.name, self.country, self.city,
                                                                   self.credit_card, self.month, self.no_year)
        success_message = self.driver.find_element(By.XPATH, self.order_success_message)
        act_message = success_message.text
        exp_message = "Thank you for your purchase!"
        print(act_message)
        try:
            if act_message == exp_message:
                self.logger.info("-----test case 017 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_017.png")
                self.logger.error("-----test case 017 is Failed------")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_017.png")
            self.logger.error("-----test case 017 is Failed------")
            assert False

    def test_case_018_validate_place_order_and_set_no_year_and_without_adding_product(self, setup_and_teardown):
        self.logger.info("-----test_case_018_validate_place_order_and_set_no_year_and_without_adding_product-----")
        self.logger.info("-------------------Verifying------------------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.click_on_place_order_to_continue_without_product(self.name, self.country, self.city,
                                                                      self.credit_card, self.month, self.no_year)
        success_message = self.driver.find_element(By.XPATH, self.order_success_message)
        act_message = success_message.text
        exp_message = "Thank you for your purchase!"
        print(act_message)
        try:
            if act_message == exp_message:
                self.logger.info("-----test case 018 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_018.png")
                self.logger.error("-----test case 018 is Failed------")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_018.png")
            self.logger.error("-----test case 018 is Failed------")
            assert False

    def test_case_019_validate_place_order_and_not_setting_any_field_and_with_adding_product(self, setup_and_teardown):
        self.logger.info("-----test_case_019_validate_place_order_and_not_setting_any_field_and_with_adding_product-----")
        self.logger.info("-------------------Verifying------------------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.click_on_place_order_to_continue_with_product(self.no_name, self.no_country, self.no_city,
                                                                   self.no_credit_card, self.no_month, self.no_year)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        expected_message = "Please fill out Name and Creditcard."
        try:
            if actual_message == expected_message:
                self.logger.info("-----test case 019 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_019.png")
                self.logger.error("-----test case 019 is Failed------")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_019.png")
            self.logger.error("-----test case 019 is Failed------")
            assert False

    def test_case_020_validate_place_order_and_not_setting_any_field_and_without_adding_product(self, setup_and_teardown):
        self.logger.info("-----test_case_018_validate_place_order_and_not_setting_any_field_and_without_adding_product-----")
        self.logger.info("-------------------Verifying------------------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.click_on_place_order_to_continue_without_product(self.no_name, self.no_country, self.no_city,
                                                                      self.no_credit_card, self.no_month, self.no_year)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        act_text = self.driver.switch_to.alert
        actual_message = act_text.text
        print(actual_message)
        self.driver.switch_to.alert.accept()
        expected_message = "Please fill out Name and Creditcard."
        try:
            if actual_message == expected_message:
                self.logger.info("-----test case 020 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_020.png")
                self.logger.error("-----test case 020 is Failed------")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_020.png")
            self.logger.error("-----test case 020 is Failed------")
            assert False

    def test_case_021_validate_click_on_place_order_x_mark(self, setup_and_teardown):
        self.logger.info("-----test_case_021_validate_click_on_place_order_x_mark-----")
        self.logger.info("-----Verifying Place order form x mark button-------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.click_on_place_order_x_mark()
        act_title = self.driver.title
        exp_title = "STORE"
        print(act_title)
        try:
            if act_title == exp_title:
                self.logger.info("-----test case 021 is Passed------")
                assert True
            else:
                time.sleep(5)
                self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_021.png")
                self.logger.error("-----test case 021 is Failed.------")
                assert False
        except TimeoutException:
            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_021.png")
            self.logger.error("-----test case 021 is Failed------")
            assert False

    def test_case_022_validate_close_button_and_set_all_fields(self, setup_and_teardown):
        self.logger.info("-----test_case_022_validate_close_button_and_set_all_fields-----")
        self.logger.info("-----Verifying Place order form x mark button-------")
        self.driver = setup_and_teardown
        self.ct_page = Cart_page(self.driver)
        self.ct_page.click_on_close_button_in_place_order_form(self.name, self.country, self.city, self.credit_card,
                                                               self.month, self.year)
        is_displayed = self.driver.find_element(By.XPATH, self.cart_page_text).is_displayed()
        try:
            if is_displayed:
                actual_text = self.driver.find_element(By.XPATH, self.cart_page_text).text
                expected_text = "Products"

                if actual_text == expected_text:
                    self.logger.info("-----test case 022 is Passed------")
                    assert True
                else:
                    time.sleep(5)
                    self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_022.png")
                    self.logger.error("-----test case 022 is Failed.------")
                    assert False
        except TimeoutException:

            time.sleep(5)
            self.driver.save_screenshot(".\\ScreenShots\\Cart_Page\\" + "test_case_022.png")
            self.logger.error("-----test case 022 is Failed. Cart Page not displayed------")
            assert False
