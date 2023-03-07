from selenium.webdriver.common.by import By
from data import config


url = config.base_url
user = config.username
password = config.password


class MyTeam():
    locator = (By.XPATH, "//span[normalize-space()='My Team']")
    summ_loc = (By.XPATH, "//ul[@class='nav topnav']")

    def __init__(self, driver):
        self.driver = driver

    def myteam(self):
        self.driver.find_element(*self.locator).click()
        self.driver.find_element(*self.summ_loc).click()

