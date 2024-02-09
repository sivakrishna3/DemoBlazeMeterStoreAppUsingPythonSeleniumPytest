# from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class Home_page:

    HOME_BUTTON = "//a[contains(text(),'Home')]"
    LOGO_HOMEPAGE = "//a/img[@src='bm.png']"
    LOGO_TEXT = "//a[@id='nava']/text()"
    PREV_SLIDE = "//a/span[@class='sr-only' and contains(text(),'Previous')]"
    NEXT_SLIDE = "//a/span[@class='sr-only' and contains(text(),'Next')]"
    HOME_TITLE = "STORE"

    CATEGORIES = "//div/a[@id='cat']"
    PREV_BUTTON = "//ul/li/button[@id='prev2']"
    NEXT_BUTTON = "//ul/li/button[@id='next2']"

    def __init__(self, driver):
        self.driver = driver

    def home_page_button(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.HOME_BUTTON)))
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()

