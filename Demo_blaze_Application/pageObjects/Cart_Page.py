from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart_page:

    CART_BUTTON = "//a[@id='cartur']"
    CART_PAGE_TITLE = "//*[@id='page-wrapper']/div/div[1]/h2"
    PLACE_ORDER = " //button[contains(text(),'Place Order')]"
    DELETE_PRODUCT = "//*[@id='tbodyid']/tr/td/a"
    NAME = "//input[@id='name']"
    COUNTRY = "//input[@id='country']"
    CITY = "//input[@id='city']"
    CREDIT_CARD = "//input[@id='card']"
    MONTH = "//input[@id='month']"
    YEAR = "//input[@id='year']"
    PURCHASE_BUTTON = "//*[@id='orderModal']/div/div/div[3]/button[2]"
    PLACE_ORDER_CLOSE_BUTTON = "//*[@id='orderModal']/div/div/div[3]/button[1]"
    PLACE_ORDER_X_MARK = "//*[@id='orderModal']/div/div/div[1]/button/span"
    ORDER_SUCCESSFUL_MSG = "/html/body/div[10]/h2"
    ORDER_SUCCESSFUL_OK_BUTTON = "/html/body/div[10]/div[7]/div/button"
    HOME_BUTTON = "//a[contains(text(),'Home')]"
    Samsung_galaxy_s6 = "//a[contains(text(),'Samsung galaxy s6')]"
    ADD_TO_CART = "//*[@id='tbodyid']/div[2]/div/a"

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
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()
        self.driver.find_element(By.XPATH, self.CART_BUTTON).click()
        self.driver.find_element(By.XPATH, self.PLACE_ORDER).click()
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

