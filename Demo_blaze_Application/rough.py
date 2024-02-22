import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# def rough(driver=None):
#     driver = Chrome()
#     driver.get("https://www.demoblaze.com/")
#     driver.implicitly_wait(10)
#     driver.maximize_window()

    # driver.find_element(By.XPATH, "//a[@id='login2' and contains(text(),'Log in')]").click()
    # driver.find_element(By.XPATH, "//input[@id='loginusername']").send_keys("adminadmin123ddddd@gmail.com")
    # driver.find_element(By.XPATH, "//input[@id='loginpassword']").send_keys("admindddddddd")
    # driver.find_element(By.XPATH, "//button[@onclick='logIn()' and contains(text(),'Log in')]").click()
    # wait = WebDriverWait(driver, 10)
    # wait.until(EC.alert_is_present())
    # al = driver.switch_to.alert
    # alert_al = al.text
    # print(alert_al)
    # driver.quit()
    # wait = WebDriverWait(driver, 10)
    # wait.until(EC.visibility_of_element_located(driver.find_element(By.XPATH, "//a[contains(text(),'Home')]")))
    # driver.find_element(By.XPATH, "//a[contains(text(),'Home')]").click()
    # # act = driver.title
    # if act == "STORE":
    #     print("STORE")
    # else:
    #     print("EROTS")

    # wait = WebDriverWait(driver, 10) wait.until(EC.visibility_of_element_located(driver.find_element(By.XPATH,
    # "//a[@class = 'nav-link' and contains(text(),'Contact')]")))

    # driver.find_element(By.XPATH, "//a[@class = 'nav-link' and contains(text(),'Contact')]").click()
    # driver.find_element(By.XPATH, "//*[@id='recipient-email']").clear()
    # driver.find_element(By.XPATH, "//*[@id='recipient-email']").send_keys("sivakrishna123@gmail.com")
    # driver.find_element(By.XPATH, "//*[@id='recipient-name']").clear()
    # driver.find_element(By.XPATH, "//*[@id='recipient-name']").send_keys("Siva Krishna")
    # driver.find_element(By.XPATH, "//*[@id='message-text']").clear()
    # driver.find_element(By.XPATH, "//*[@id='message-text']").send_keys("This is a message")
    # driver.find_element(By.XPATH, "//button[contains(text(),'Send message') and //*["
    #                               "@id='exampleModal']/div/div/div/button]").click()
    # al = driver.switch_to.alert
    # al_message = al.text
    # print(al_message)

    # driver.find_element(By.XPATH, "//a[@class = 'nav-link' and contains(text(),'Contact')]").click()
    # wait = WebDriverWait(driver, 10)
    # wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[1]/h5")))
    # al = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/h5")
    # # al_text = al.text
    # # print(al.text)
    # wait = WebDriverWait(driver, 10)
    # wait.until(EC.visibility_of_element_located("//a/span[contains(text(),'Previous')]"))
    # driver.find_element(By.XPATH, "//a/span[contains(text(),'Previous')]").click()
    # driver.find_element(By.XPATH, "//a/span[contains(text(),'Previous')]").click()

#     print(driver.find_element(By.XPATH, "//div[@id='contcont']//a[2]").text)
#     table = driver.find_element((By.XPATH, "//div[@id='tbodyid']"))
#
#
#     driver.quit()
#
#
# # rough()
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# class HomePage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.phones_link = (By.XPATH, "//a[@id='itemc']")
#
#     def navigate_to_phones_page(self):
#         self.driver.find_element(By.XPATH, self.phones_link).click()
#
#
# class PhonesPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.phone_table = (By.XPATH, "//div[@class='container']/div[2]/div/div[2]/div[2]/div/table")
#
#     def get_phone_info(self):
#
#         phone_info_list = []
#         phone_table = self.driver.find_element(By.XPATH, self.phone_table)
#         rows = phone_table.find_elements(By.TAG_NAME, "tr")[1:]  # Skip the header row
#         for row in rows:
#             columns = row.find_elements(By.TAG_NAME, "td")
#             if columns:
#                 phone_id = columns[0].text
#                 brand = columns[1].text
#                 model = columns[2].text
#                 price = columns[3].text
#
#                 phone_info = {
#                     "Phone ID": phone_id,
#                     "Brand": brand,
#                     "Model": model,
#                     "Price": price
#                 }
#
#                 phone_info_list.append(phone_info)
#         print(phone_info_list)
#         return phone_info_list
#
#
# if __name__ == "__main__":
#     driver = webdriver.Chrome()
#     driver.get("https://www.demoblaze.com/#")
#
#     home_page = HomePage(driver)
#     home_page.navigate_to_phones_page()
#
#     phones_page = PhonesPage(driver)
#     phone_data = phones_page.get_phone_info()
#
#     for phone_info in phone_data:
#         print("-----")
#         for key, value in phone_info.items():
#             print(f"{key}: {value}")
#
#     driver.quit()
