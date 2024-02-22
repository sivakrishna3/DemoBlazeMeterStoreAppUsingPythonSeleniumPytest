import self
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time


class Login_page:

    def __init__(self, driver):
        self.driver = driver

    def driver_setup(self):
        self.driver = Chrome()
        self.driver.get(url='https://www.saucedemo.com/')
        self.driver.maximize_window()
        yield

        return self.driver

    def LoginPage_TC_01(self, driver_setup):
        self.driver = driver_setup
        self.driver.find_element(By.XPATH, '*//input[@id="user-name"]').send_keys('standard_user')
        self.driver.find_element(By.XPATH, '*//input[@id="password"]').send_keys('secret_sauce')
        self.driver.find_element(By.XPATH, "//input[contains(@class,'submit')]").click()
        time.sleep(5)
        try:
            products = self.driver.find_element(By.XPATH, "//span[text()='Products']")
            print(products.text)
            if products.text == 'Products':
                print('succesfully login')
                time.sleep(5)
                menu_button = self.driver.find_element(By.XPATH, '//button[contains(@id,"menu-btn")]')
                menu_button.click()
                time.sleep(4)
                logout = self.driver.find_element(By.XPATH, '//a[text()="Logout"]')
                logout.click()
                print('succesfully logout')
            else:
                print('no data found')
        except Exception:
            print('INVALID CREDENTIALS')

    def LoginPage_TC_02(self, driver_setup):
        self.driver = driver_setup

        self.driver.find_element(By.XPATH, '*//input[@id="user-name"]').clear()
        self.driver.find_element(By.XPATH, '*//input[@id="password"]').clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '*//input[@id="user-name"]').send_keys('hello123')
        self.driver.find_element(By.XPATH, '*//input[@id="password"]').send_keys('secret_sauce')
        self.driver.find_element(By.XPATH, "//input[contains(@class,'submit')]").click()
        time.sleep(5)
        try:
            products = self.driver.find_element(By.XPATH, "//span[text()='Products']")
            print(products.text)
            if products.text == 'Products':
                print('succesfully login')
                time.sleep(5)
                menu_button = self.driver.find_element(By.XPATH, '//button[contains(@id,"menu-btn")]')
                menu_button.click()
                time.sleep(4)
                logout = self.driver.find_element(By.XPATH, '//a[text()="Logout"]')
                logout.click()
                print('succesfully logout')
            else:
                print('no data found')
        except Exception:
            print('INVALID CREDENTIALS')

    def LoginPage_TC_03(self, driver_setup):
        self.driver = driver_setup
        self.driver.find_element(By.XPATH, '*//input[@id="user-name"]').clear()
        self.driver.find_element(By.XPATH, '*//input[@id="password"]').clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '*//input[@id="user-name"]').send_keys('standard_user')
        self.driver.find_element(By.XPATH, '*//input[@id="password"]').send_keys('password')
        self.driver.find_element(By.XPATH, "//input[contains(@class,'submit')]").click()
        try:
            products = self.driver.find_element(By.XPATH, "//span[text()='Products']")
            print(products.text)
            if products.text == 'Products':
                print('succesfully login')
                time.sleep(5)
                menu_button = self.driver.find_element(By.XPATH, '//button[contains(@id,"menu-btn")]')
                menu_button.click()
                time.sleep(4)
                logout = self.driver.find_element(By.XPATH, '//a[text()="Logout"]')
                logout.click()
                print('succesfully logout')
            else:
                print('no data found')
        except Exception:
            print('INVALID CREDENTIALS')

    def LoginPage_TC_04(self, driver_setup):
        self.driver = driver_setup
        self.driver.find_element(By.XPATH, '*//input[@id="user-name"]').clear()
        self.driver.find_element(By.XPATH, '*//input[@id="password"]').clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '*//input[@id="user-name"]').send_keys('hello123')
        self.driver.find_element(By.XPATH, '*//input[@id="password"]').send_keys('password')
        self.driver.find_element(By.XPATH, "//input[contains(@class,'submit')]").click()
        time.sleep(5)
        try:
            products = self.driver.find_element(By.XPATH, "//span[text()='Products']")
            print(products.text)
            if products.text == 'Products':
                print('succesfully login')
                time.sleep(5)
                menu_button = self.driver.find_element(By.XPATH, '//button[contains(@id,"menu-btn")]')
                menu_button.click()
                time.sleep(4)
                logout = self.driver.find_element(By.XPATH, '//a[text()="Logout"]')
                logout.click()
                print('succesfully logout')
            else:
                print('no data found')
        except Exception:
            print('INVALID CREDENTIALS')

    def LoginPage_TC_05(self, driver_setup):
        self.driver = driver_setup
        self.driver.find_element(By.XPATH, '*//input[@id="user-name"]').clear()
        self.driver.find_element(By.XPATH, '*//input[@id="password"]').clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '*//input[@id="user-name"]').send_keys()
        self.driver.find_element(By.XPATH, '*//input[@id="password"]').send_keys('secret_sauce')
        self.driver.find_element(By.XPATH, "//input[contains(@class,'submit')]").click()
        time.sleep(5)
        try:
            products = self.driver.find_element(By.XPATH, "//span[text()='Products']")
            print(products.text)
            if products.text == 'Products':
                print('succesfully login')
                time.sleep(5)
                menu_button = self.driver.find_element(By.XPATH, '//button[contains(@id,"menu-btn")]')
                menu_button.click()
                time.sleep(4)
                logout = self.driver.find_element(By.XPATH, '//a[text()="Logout"]')
                logout.click()
                print('succesfully logout')
            else:
                print('no data found')
        except Exception:
            print('INVALID CREDENTIALS')

    def LoginPage_TC_06(self, driver_setup):
        self.driver = driver_setup
        self.driver.find_element(By.XPATH, '*//input[@id="user-name"]').clear()
        self.driver.find_element(By.XPATH, '*//input[@id="password"]').clear()
        time.sleep(2)
        print('sixth')
        self.driver.find_element(By.XPATH, '*//input[@id="user-name"]').send_keys('standard_user')
        self.driver.find_element(By.XPATH, '*//input[@id="password"]').send_keys()
        self.driver.find_element(By.XPATH, "//input[contains(@class,'submit')]").click()
        time.sleep(5)
        try:
            products = self.driver.find_element(By.XPATH, "//span[text()='Products']")
            print(products.text)
            if products.text == 'Products':
                print('succesfully login,sixth')
                time.sleep(5)
                menu_button = self.driver.find_element(By.XPATH, '//button[contains(@id,"menu-btn")]')
                menu_button.click()
                time.sleep(4)
                logout = self.driver.find_element(By.XPATH, '//a[text()="Logout"]')
                logout.click()
                print('succesfully logout,sixth')
            else:
                print('no data found')
        except Exception:
            print('INVALID CREDENTIALS')

    def LoginPage_TC_07(self, driver_setup):
        self.driver = driver_setup
        self.driver.find_element(By.XPATH, '*//input[@id="user-name"]').clear()
        self.driver.find_element(By.XPATH, '*//input[@id="password"]').clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '*//input[@id="user-name"]').send_keys()
        self.driver.find_element(By.XPATH, '*//input[@id="password"]').send_keys()
        self.driver.find_element(By.XPATH, "//input[contains(@class,'submit')]").click()
        time.sleep(5)
        try:
            products = self.driver.find_element(By.XPATH, "//span[text()='Products']")
            print(products.text)
            if products.text == 'Products':
                print('succesfully login')
                time.sleep(5)
                menu_button = self.driver.find_element(By.XPATH, '//button[contains(@id,"menu-btn")]')
                menu_button.click()
                time.sleep(4)
                logout = self.driver.find_element(By.XPATH, '//a[text()="Logout"]')
                logout.click()
                print('succesfully logout')
            else:
                print('no data found')
        except Exception:
            print('INVALID CREDENTIALS')


obj_ref = Login_page(self.driver)
obj_ref.driver_setup()
obj_ref.LoginPage_TC_01()
obj_ref.LoginPage_TC_02()
obj_ref.LoginPage_TC_03()
obj_ref.LoginPage_TC_04()
obj_ref.LoginPage_TC_05()
obj_ref.LoginPage_TC_06()
obj_ref.LoginPage_TC_07()




