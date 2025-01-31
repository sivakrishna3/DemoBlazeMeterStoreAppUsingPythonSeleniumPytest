import time
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import ReadConfig


class About_us_Page:

    data = ReadConfig.get_json_data()
    try:
        ABOUT_US_BUTTON = data['About_Us_Page']["ABOUT_US_BUTTON"]
        VIDEO_BUTTON = data['About_Us_Page']["VIDEO_BUTTON"]
        VIDEO_PAUSE_BUTTON = data['About_Us_Page']["VIDEO_PAUSE_BUTTON"]
        VOLUME_MUTE_BUTTON = data['About_Us_Page']["VOLUME_MUTE_BUTTON"]
        VOLUME_BUTTON = data['About_Us_Page']["VOLUME_BUTTON"]
        VIDEO_CONTROL_BUTTON = data['About_Us_Page']["VIDEO_CONTROL_BUTTON"]
        SCREEN_PIC_IN_PIC_BUTTON = data['About_Us_Page']["SCREEN_PIC_IN_PIC_BUTTON"]
        FULL_SCREEN_BUTTON = data['About_Us_Page']["FULL_SCREEN_BUTTON"]
        VIDEO_CLOSE_BUTTON = data['About_Us_Page']["VIDEO_CLOSE_BUTTON"]
        VIDEO_CLOSE_X_MARK = data['About_Us_Page']["VIDEO_CLOSE_X_MARK"]
        VOLUME_SLIDER = data['About_Us_Page']["VOLUME_SLIDER"]
        video_pause_clause = data["About_Us_Page"]["video_pause_clause"]
        volume_mute_clause = data["About_Us_Page"]["volume_mute_clause"]
        video_pic_in_pic_clause = data["About_Us_Page"]["video_pic_in_pic_clause"]
        video_full_screen_clause = data["About_Us_Page"]["video_full_screen_clause"]
    except Exception as e:
        print(f"{e}: No such element found.")

    def __init__(self, driver):
        self.driver = driver

    def click_on_about_us_button(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until((EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON))))
        self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON).click()
        # self.driver.find_element(By.XPATH, self.About_us_open_message)

    def click_on_video_close_button(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until((EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON))))
        self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON).click()
        self.driver.find_element(By.XPATH, self.VIDEO_BUTTON).click()
        time.sleep(3)
        # self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_BUTTON).click()

    def click_on_video_close_x_mark(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until((EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON))))
        self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON).click()
        self.driver.find_element(By.XPATH, self.VIDEO_BUTTON).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_X_MARK).click()

    def click_on_video_button(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until((EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON))))
        self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON).click()
        self.driver.find_element(By.XPATH, self.VIDEO_BUTTON).click()
        time.sleep(3)

    def click_on_video_pause_button(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until((EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON))))
        self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON).click()
        self.driver.find_element(By.XPATH, self.VIDEO_BUTTON).click()
        time.sleep(3)
        pause_button = self.driver.find_element(By.CLASS_NAME, self.video_pause_clause)
        ac = ActionChains(self.driver)
        ac.move_to_element(pause_button).click().perform()
        time.sleep(3)
        # self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_BUTTON).click()

    def click_on_volume_mute_button(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until((EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON))))
        self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON).click()
        self.driver.find_element(By.XPATH, self.VIDEO_BUTTON).click()
        time.sleep(3)
        mute_button = self.driver.find_element(By.CLASS_NAME, self.volume_mute_clause)
        ac = ActionChains(self.driver)
        ac.move_to_element(mute_button).click().perform()
        time.sleep(3)
        # self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_BUTTON).click()

    def click_on_pic_in_pic_button(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until((EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON))))
        self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON).click()
        self.driver.find_element(By.XPATH, self.VIDEO_BUTTON).click()
        time.sleep(3)
        pic_in_pic_button = self.driver.find_element(By.CLASS_NAME, self.video_pic_in_pic_clause)
        ac = ActionChains(self.driver)
        ac.move_to_element(pic_in_pic_button).click().perform()
        time.sleep(3)
        # self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_BUTTON).click()

    def click_on_full_screen_button(self):
        self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON).click()
        self.driver.find_element(By.XPATH, self.VIDEO_BUTTON).click()
        time.sleep(3)
        full_screen = self.driver.find_element(By.CLASS_NAME, self.video_full_screen_clause)
        ac = ActionChains(self.driver)
        ac.move_to_element(full_screen).click().perform()
        time.sleep(3)
        # self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_BUTTON).click()

