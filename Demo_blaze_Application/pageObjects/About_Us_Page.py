import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class About_us_Page:
    ABOUT_US_BUTTON = "//*[@id='navbarExample']/ul/li[3]/a"
    VIDEO_BUTTON = "//*[@id='example-video']/button"
    VIDEO_PAUSE_BUTTON = "//button[@title='Pause']//span[@class='vjs-icon-placeholder']"
    VOLUME_MUTE_BUTTON = "//*[@id='example-video']/div[4]/div[1]"
    VOLUME_BUTTON = "//*[@id='example-video']/div[4]/div[1]/div/div/div"
    VIDEO_CONTROL_BUTTON = "//*[@id='example-video']/div[4]/div[5]"
    SCREEN_PIC_IN_PIC_BUTTON = "//*[@id='example-video']/div[4]/button[3]"
    FULL_SCREEN_BUTTON = "//*[@id='example-video']/div[4]/button[4]/span[1]"
    VIDEO_CLOSE_BUTTON = "//*[@id='videoModal']/div/div/div[3]/button"
    VIDEO_CLOSE_X_MARK = "//*[@id='videoModal']/div/div/div[1]/button/span"

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
        self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_BUTTON).click()

    def click_on_video_close_x_mark(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until((EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON))))
        self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON).click()
        # self.driver.fine_element(By.XPATH, self.VIDEO_CLOSE_X_MARK).click()

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
        ac = ActionChains(self.driver)
        ac.move_to_element(self.driver.find_element(By.CLASS_NAME, "vjs-play-control vjs-control vjs-button vjs-playing"))
        ac.perform()
        self.driver.find_element(By.XPATH, self.VIDEO_PAUSE_BUTTON).click()

    def click_on_volume_mute_button(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until((EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON))))
        self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON).click()
        self.driver.find_element(By.XPATH, self.VIDEO_BUTTON).click()
        time.sleep(5)
        ac = ActionChains(self.driver)
        ac.move_to_element(self.driver.find_element(By.CLASS_NAME, "vjs-icon-placeholder"))
        ac.perform()
        self.driver.find_element(By.XPATH, self.VIDEO_BUTTON).click()
        ac = ActionChains(self.driver)
        ac.move_to_element(self.driver.find_element(By.CLASS_NAME, "vjs-icon-placeholder"))
        ac.perform()
        self.driver.find_element(By.XPATH, self.VOLUME_MUTE_BUTTON).click()

    def click_on_volume_button(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until((EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON))))
        self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON).click()
        self.driver.find_element(By.XPATH, self.VIDEO_BUTTON).click()
        time.sleep(5)
        ac = ActionChains(self.driver)
        ac.move_to_element(self.driver.find_element(By.CLASS_NAME, "vjs-icon-placeholder"))
        ac.perform()
        self.driver.find_element(By.XPATH, self.VIDEO_BUTTON).click()
        ac = ActionChains(self.driver)
        ac.move_to_element(self.driver.find_element(By.CLASS_NAME, "vjs-icon-placeholder"))
        ac.perform()
        self.driver.find_element(By.XPATH, self.VIDEO_BUTTON).click()
        ac = ActionChains(self.driver)
        ac.move_to_element(self.driver.find_element(By.CLASS_NAME, "vjs-volume-level"))
        ac.perform()
        self.driver.find_element(By.XPATH, self.VOLUME_BUTTON).click()

    def click_on_pic_in_pic_button(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until((EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON))))
        self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON).click()
        self.driver.find_element(By.XPATH, self.VIDEO_BUTTON).click()
        self.driver.find_element(By.XPATH, self.SCREEN_PIC_IN_PIC_BUTTON).click()

    def click_on_full_screen_button(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until((EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON))))
        self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON).click()
        self.driver.find_element(By.XPATH, self.VIDEO_BUTTON).click()
        self.driver.find_element(By.XPATH, self.FULL_SCREEN_BUTTON).click()

    # def click_on_video_control_bar(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until((EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON))))
    #     self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON).click()
    #     self.driver.find_element(By.XPATH, self.VIDEO_BUTTON).click()
    #     self.driver.find_element(By.XPATH, self.VIDEO_CONTROL_BUTTON).click()
