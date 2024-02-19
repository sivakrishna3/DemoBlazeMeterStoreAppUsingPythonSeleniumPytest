import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class About_us_Page:
    ABOUT_US_BUTTON = "//*[@id='navbarExample']/ul/li[3]/a"
    VIDEO_BUTTON = "//*[@id='example-video']/button"
    VIDEO_PAUSE_BUTTON = "//button[@title='Pause']//span[@class='vjs-icon-placeholder']"
    VOLUME_MUTE_BUTTON = "//button[@title='Mute']//span[@class='vjs-icon-placeholder']"
    VOLUME_BUTTON = "//*[@id='example-video']/div[4]/div[1]/div/div/div"
    VIDEO_CONTROL_BUTTON = "//*[@id='example-video']/div[4]/div[5]"
    SCREEN_PIC_IN_PIC_BUTTON = "//*[@id='example-video']/div[4]/button[3]"
    FULL_SCREEN_BUTTON = "//*[@id='example-video']/div[4]/button[4]/span[1]"
    VIDEO_CLOSE_BUTTON = "//*[@id='videoModal']/div/div/div[3]/button"
    VIDEO_CLOSE_X_MARK = "//*[@id='videoModal']/div/div/div[1]/button/span"
    VOLUME_SLIDER = "//button[@title='Mute']//span[@class='vjs-icon-placeholder']"
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
        time.sleep(3)
        pause_button = self.driver.find_element(By.CLASS_NAME, "vjs-play-control")
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
        mute_button = self.driver.find_element(By.CLASS_NAME, "vjs-mute-control")
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
        pic_in_pic_button = self.driver.find_element(By.CLASS_NAME, "vjs-picture-in-picture-control")
        ac = ActionChains(self.driver)
        ac.move_to_element(pic_in_pic_button).click().perform()
        time.sleep(3)
        # self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_BUTTON).click()

    def click_on_full_screen_button(self):
        self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON).click()
        self.driver.find_element(By.XPATH, self.VIDEO_BUTTON).click()
        time.sleep(3)
        full_screen = self.driver.find_element(By.CLASS_NAME, "vjs-fullscreen-control")
        ac = ActionChains(self.driver)
        ac.move_to_element(full_screen).click().perform()
        time.sleep(3)
        # self.driver.find_element(By.XPATH, self.VIDEO_CLOSE_BUTTON).click()

    def click_on_video_volume_handle_button(self, volume):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until((EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON))))
        self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON).click()
        self.driver.find_element(By.XPATH, self.VIDEO_BUTTON).click()
        time.sleep(5)
        volume_slider = self.driver.find_element(By.CLASS_NAME, "vjs-mute-control")
        ac = ActionChains(self.driver)
        ac.move_to_element(volume_slider).perform()
        slider = self.driver.find_element(By.XPATH, self.VOLUME_SLIDER)
        current_position = slider.get_attribute("aria-valuenow")
        new_position = int(current_position) + volume
        ac = ActionChains(self.driver)
        ac.click_and_hold(slider).move_by_offset(new_position,0).release().perform()
        time.sleep(3)




    # def click_on_video_control_bar(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until((EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON))))
    #     self.driver.find_element(By.XPATH, self.ABOUT_US_BUTTON).click()
    #     self.driver.find_element(By.XPATH, self.VIDEO_BUTTON).click()
    #     self.driver.find_element(By.XPATH, self.VIDEO_CONTROL_BUTTON).click()
