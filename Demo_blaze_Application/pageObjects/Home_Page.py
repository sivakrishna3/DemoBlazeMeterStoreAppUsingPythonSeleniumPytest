import json

from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Home_page:
    json_file_path = "./Locators/locators.json"
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    HOME_BUTTON = data["Home_Page"]["HOME_BUTTON"]
    LOGO_HOMEPAGE = data["Home_Page"]["LOGO_HOMEPAGE"]
    PREV_SLIDE = data["Home_Page"]["PREV_SLIDE"]
    NEXT_SLIDE = data["Home_Page"]["NEXT_SLIDE"]
    CATEGORIES = data["Home_Page"]["CATEGORIES"]
    PHONES = data["Home_Page"]["PHONES"]
    LAPTOPS = data["Home_Page"]["LAPTOPS"]
    MONITORS = data["Home_Page"]["MONITORS"]
    PREV_BUTTON = data["Home_Page"]["PREV_BUTTON"]
    NEXT_BUTTON = data["Home_Page"]["NEXT_BUTTON"]
    Add_To_Cart = data["Home_Page"]["Add_To_Cart"]

    # Phones details
    Samsung_galaxy_s6 = data["Phones"]["Samsung_galaxy_s6"]
    Nokia_lumia_1520 = data["Phones"]["Nokia_lumia_1520"]
    Nexus_6 = data["Phones"]["Nexus_6"]
    Samsung_galaxy_s7 = data["Phones"]["Samsung_galaxy_s7"]
    Iphone_6_32_gb = data["Phones"]["Iphone_6_32_gb"]
    Sony_xperia_z5 = data["Phones"]["Sony_xperia_z5"]
    HTC_One_M9 = data["Phones"]["HTC_One_M9"]

    # Laptops details
    Sony_vaio_i5 = data["Laptops"]["Sony_vaio_i5"]
    Sony_vaio_i7 = data["Laptops"]["Sony_vaio_i7"]
    MacBook_air = data["Laptops"]["MacBook_air"]
    Dell_i7_8_gb = data["Laptops"]["Dell_i7_8_gb"]
    _2017_Dell_15_6_Inch = data["Laptops"]["_2017_Dell_15_6_Inch"]
    MacBook_Pro = data["Laptops"]["MacBook_Pro"]

    # Monitors details
    Apple_monitor_24 = data["Monitors"]["Apple_monitor_24"]
    ASUS_Full_HD = data["Monitors"]["ASUS_Full_HD"]

    def __init__(self, driver):
        self.driver = driver

    def click_on_home_page_button(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.HOME_BUTTON)))
        self.driver.find_element(By.XPATH, self.HOME_BUTTON).click()

    def click_on_home_page_logo(self):
        self.driver.find_element(By.XPATH, self.LOGO_HOMEPAGE).click()

    def click_on_next_and_previous_slide_buttons(self):
        self.driver.find_element(By.XPATH, self.PREV_SLIDE).click()
        self.driver.find_element(By.XPATH, self.NEXT_SLIDE).click()
        self.driver.find_element(By.XPATH, self.PREV_SLIDE).click()
        self.driver.find_element(By.XPATH, self.NEXT_SLIDE).click()

    def click_on_home_page_next_and_previous_button(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until((EC.visibility_of_element_located(self.driver.execute_script("window.scrollBy(0,1850);"))))
        # self.driver.execute_script("window.scrollBy(0,1850);")
        self.driver.find_element(By.XPATH, self.NEXT_BUTTON).click()
        # wait = WebDriverWait(self.driver, 10)
        # wait.until((EC.visibility_of_element_located(self.driver.execute_script("window.scrollBy(0,1850);"))))
        # self.driver.execute_script("window.scrollBy(0,1850);")
        self.driver.find_element(By.XPATH, self.PREV_BUTTON).click()

    def click_on_categories_button(self):
        self.driver.find_element(By.XPATH, self.CATEGORIES).click()

    def click_on_phones_button_from_categories(self):
        self.driver.find_element(By.XPATH, self.PHONES).click()

    def click_on_Laptops_button_from_categories(self):
        self.driver.find_element(By.XPATH, self.LAPTOPS).click()

    def click_on_Monitors_button_from_categories(self):
        self.driver.find_element(By.XPATH, self.MONITORS).click()

    def Add_Samsung_galaxy_s6(self):
        self.driver.find_element(By.XPATH, self.PHONES).click()
        self.driver.find_element(By.XPATH, self.Samsung_galaxy_s6).click()
        self.driver.find_element(By.XPATH, self.Add_To_Cart).click()

    def Add_Nokia_lumia_1520(self):
        self.driver.find_element(By.XPATH, self.PHONES).click()
        self.driver.find_element(By.XPATH, self.Nokia_lumia_1520).click()
        self.driver.find_element(By.XPATH, self.Add_To_Cart).click()

    def Add_Nexus_6(self):
        self.driver.find_element(By.XPATH, self.PHONES).click()
        self.driver.find_element(By.XPATH, self.Nexus_6).click()
        self.driver.find_element(By.XPATH, self.Add_To_Cart).click()

    def Add_Samsung_galaxy_s7(self):
        self.driver.find_element(By.XPATH, self.PHONES).click()
        self.driver.execute_script("window.scrollBy(0,850);")
        self.driver.find_element(By.XPATH, self.Samsung_galaxy_s7).click()
        self.driver.find_element(By.XPATH, self.Add_To_Cart).click()

    def Add_Iphone_6_32_gb(self):
        self.driver.find_element(By.XPATH, self.PHONES).click()
        self.driver.execute_script("window.scrollBy(0,850);")
        self.driver.find_element(By.XPATH, self.Iphone_6_32_gb).click()
        self.driver.find_element(By.XPATH, self.Add_To_Cart).click()

    def Add_Sony_xperia_z5(self):
        self.driver.find_element(By.XPATH, self.PHONES).click()
        self.driver.execute_script("window.scrollBy(0,850);")
        self.driver.find_element(By.XPATH, self.Sony_xperia_z5).click()
        self.driver.find_element(By.XPATH, self.Add_To_Cart).click()

    def Add_HTC_One_M9(self):
        self.driver.find_element(By.XPATH, self.PHONES).click()
        self.driver.execute_script("window.scrollBy(0,850);")
        self.driver.find_element(By.XPATH, self.HTC_One_M9).click()
        self.driver.find_element(By.XPATH, self.Add_To_Cart).click()

    def Add_Sony_vaio_i5(self):
        self.driver.find_element(By.XPATH, self.LAPTOPS).click()
        self.driver.find_element(By.XPATH, self.Sony_vaio_i5).click()
        self.driver.find_element(By.XPATH, self.Add_To_Cart).click()

    def Add_Sony_vaio_i7(self):
        self.driver.find_element(By.XPATH, self.LAPTOPS).click()
        self.driver.find_element(By.XPATH, self.Sony_vaio_i7).click()
        self.driver.find_element(By.XPATH, self.Add_To_Cart).click()

    def Add_MacBook_air(self):
        self.driver.find_element(By.XPATH, self.LAPTOPS).click()
        self.driver.find_element(By.XPATH, self.MacBook_air).click()
        self.driver.find_element(By.XPATH, self.Add_To_Cart).click()

    def Add_Dell_i7_8_gb(self):
        self.driver.find_element(By.XPATH, self.LAPTOPS).click()
        self.driver.execute_script("window.scrollBy(0,900);")
        self.driver.find_element(By.XPATH, self.Dell_i7_8_gb).click()
        self.driver.find_element(By.XPATH, self.Add_To_Cart).click()

    def Add_2017_Dell_15_6_Inch(self):
        self.driver.find_element(By.XPATH, self.LAPTOPS).click()
        self.driver.execute_script("window.scrollBy(0,900);")
        self.driver.find_element(By.XPATH, self._2017_Dell_15_6_Inch).click()
        self.driver.find_element(By.XPATH, self.Add_To_Cart).click()

    def Add_MacBook_Pro(self):
        self.driver.find_element(By.XPATH, self.LAPTOPS).click()
        self.driver.execute_script("window.scrollBy(0,900);")
        self.driver.find_element(By.XPATH, self.MacBook_Pro).click()
        self.driver.find_element(By.XPATH, self.Add_To_Cart).click()

    def Add_Apple_monitor_24(self):
        self.driver.find_element(By.XPATH, self.MONITORS).click()
        self.driver.find_element(By.XPATH, self.Apple_monitor_24).click()
        self.driver.find_element(By.XPATH, self.Add_To_Cart).click()

    def Add_ASUS_Full_HD(self):
        self.driver.find_element(By.XPATH, self.MONITORS).click()
        self.driver.find_element(By.XPATH, self.ASUS_Full_HD).click()
        self.driver.find_element(By.XPATH, self.Add_To_Cart).click()
