from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import ReadConfig


class Cart_page:
    data = ReadConfig.get_json_data()
    try:
        CART_BUTTON = data["Cart_Page"]["CART_BUTTON"]
        CART_PAGE_TITLE = data["Cart_Page"]["CART_PAGE_TITLE"]
        PLACE_ORDER = data["Cart_Page"]["PLACE_ORDER"]
        DELETE_PRODUCT = data["Cart_Page"]["DELETE_PRODUCT"]
        NAME = data["Cart_Page"]["NAME"]
        COUNTRY = data["Cart_Page"]["COUNTRY"]
        CITY = data["Cart_Page"]["CITY"]
        CREDIT_CARD = data["Cart_Page"]["CREDIT_CARD"]
        MONTH = data["Cart_Page"]["MONTH"]
        YEAR = data["Cart_Page"]["YEAR"]
        PURCHASE_BUTTON = data["Cart_Page"]["PURCHASE_BUTTON"]
        PLACE_ORDER_CLOSE_BUTTON = data["Cart_Page"]["PLACE_ORDER_CLOSE_BUTTON"]
        PLACE_ORDER_X_MARK = data["Cart_Page"]["PLACE_ORDER_X_MARK"]
        ORDER_SUCCESSFUL_MSG = data["Cart_Page"]["ORDER_SUCCESSFUL_MSG"]
        ORDER_SUCCESSFUL_OK_BUTTON = data["Cart_Page"]["ORDER_SUCCESSFUL_OK_BUTTON"]
        HOME_BUTTON = data["Cart_Page"]["HOME_BUTTON"]
        Samsung_galaxy_s6 = data["Cart_Page"]["Samsung_galaxy_s6"]
        ADD_TO_CART = data["Cart_Page"]["ADD_TO_CART"]
    except Exception as e:
        print(f"{e}: No such element found in json file.")

    def __init__(self, driver):
        self.driver = driver

    def clicking_on_cart_button(self):
        self.driver.find_element(By.XPATH, self.CART_BUTTON).click()

    def clicking_on_place_order_button(self):
        self.driver.find_element(By.XPATH, self.CART_BUTTON).click()
        self.driver.find_element(By.XPATH, self.PLACE_ORDER).click()

    def clicking_on_delete_option(self):
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()
        self.driver.find_element(By.XPATH, self.Samsung_galaxy_s6).click()
        self.driver.find_element(By.XPATH, self.ADD_TO_CART).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
        # self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()
        self.driver.find_element(By.XPATH, self.CART_BUTTON).click()
        self.driver.find_element(By.XPATH, self.DELETE_PRODUCT).click()

    def adding_product_to_cart(self):
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()
        self.driver.find_element(By.XPATH, self.Samsung_galaxy_s6).click()
        self.driver.find_element(By.XPATH, self.ADD_TO_CART).click()

    def click_on_place_order_to_continue_with_product(self, name, country, city, creditcard, month, year):
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()
        self.driver.find_element(By.XPATH, self.Samsung_galaxy_s6).click()
        self.driver.find_element(By.XPATH, self.ADD_TO_CART).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()
        self.driver.find_element(By.XPATH, self.CART_BUTTON).click()
        self.driver.find_element(By.XPATH, self.PLACE_ORDER).click()
        self.driver.find_element(By.XPATH, self.NAME).clear()
        self.driver.find_element(By.XPATH, self.NAME).send_keys(name)
        self.driver.find_element(By.XPATH, self.COUNTRY).clear()
        self.driver.find_element(By.XPATH, self.COUNTRY).send_keys(country)
        self.driver.find_element(By.XPATH, self.CITY).clear()
        self.driver.find_element(By.XPATH, self.CITY).send_keys(city)
        self.driver.find_element(By.XPATH, self.CREDIT_CARD).clear()
        self.driver.find_element(By.XPATH, self.CREDIT_CARD).send_keys(creditcard)
        self.driver.find_element(By.XPATH, self.MONTH).clear()
        self.driver.find_element(By.XPATH, self.MONTH).send_keys(month)
        self.driver.find_element(By.XPATH, self.YEAR).clear()
        self.driver.find_element(By.XPATH, self.YEAR).send_keys(year)
        self.driver.find_element(By.XPATH, self.PURCHASE_BUTTON).click()

    def click_on_place_order_to_continue_without_product(self, name, country, city, creditcard, month, year):
        self.driver.find_element(By.XPATH, self.CART_BUTTON).click()
        self.driver.find_element(By.XPATH, self.PLACE_ORDER).click()
        self.driver.find_element(By.XPATH, self.NAME).clear()
        self.driver.find_element(By.XPATH, self.NAME).send_keys(name)
        self.driver.find_element(By.XPATH, self.COUNTRY).clear()
        self.driver.find_element(By.XPATH, self.COUNTRY).send_keys(country)
        self.driver.find_element(By.XPATH, self.CITY).clear()
        self.driver.find_element(By.XPATH, self.CITY).send_keys(city)
        self.driver.find_element(By.XPATH, self.CREDIT_CARD).clear()
        self.driver.find_element(By.XPATH, self.CREDIT_CARD).send_keys(creditcard)
        self.driver.find_element(By.XPATH, self.MONTH).clear()
        self.driver.find_element(By.XPATH, self.MONTH).send_keys(month)
        self.driver.find_element(By.XPATH, self.YEAR).clear()
        self.driver.find_element(By.XPATH, self.YEAR).send_keys(year)
        self.driver.find_element(By.XPATH, self.PURCHASE_BUTTON).click()

    def click_on_close_button_in_place_order_form(self, name, country, city, creditcard, month, year):
        self.driver.find_element(By.XPATH, self.CART_BUTTON).click()
        self.driver.find_element(By.XPATH, self.PLACE_ORDER).click()
        self.driver.find_element(By.XPATH, self.NAME).clear()
        self.driver.find_element(By.XPATH, self.NAME).send_keys(name)
        self.driver.find_element(By.XPATH, self.COUNTRY).clear()
        self.driver.find_element(By.XPATH, self.COUNTRY).send_keys(country)
        self.driver.find_element(By.XPATH, self.CITY).clear()
        self.driver.find_element(By.XPATH, self.CITY).send_keys(city)
        self.driver.find_element(By.XPATH, self.CREDIT_CARD).clear()
        self.driver.find_element(By.XPATH, self.CREDIT_CARD).send_keys(creditcard)
        self.driver.find_element(By.XPATH, self.MONTH).clear()
        self.driver.find_element(By.XPATH, self.MONTH).send_keys(month)
        self.driver.find_element(By.XPATH, self.YEAR).clear()
        self.driver.find_element(By.XPATH, self.YEAR).send_keys(year)
        self.driver.find_element(By.XPATH, self.PLACE_ORDER_CLOSE_BUTTON).click()

    def click_on_place_order_x_mark(self):
        self.driver.find_element(By.XPATH, self.CART_BUTTON).click()
        self.driver.find_element(By.XPATH, self.PLACE_ORDER).click()
        self.driver.find_element(By.XPATH, self.PLACE_ORDER_X_MARK).click()
