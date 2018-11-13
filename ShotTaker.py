from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import util

class ShotTaker():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.fullscreen_window()

    def destroy(self):
        self.driver.quit()

    def take(self,url,out_path):
        self.driver.get(url)
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        util.fullpage_screenshot(self.driver,out_path)

