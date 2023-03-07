from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from data import config


url = config.base_url
user = config.username
password = config.password


class MeFunctionality():

    me_function = (By.XPATH, "//span[normalize-space()='Me']")
    leave = (By.XPATH, "//a[@routerlink='leave']")
    attendence = (By.XPATH, "//a[@routerlink='attendance']")
    performance = (By.CSS_SELECTOR, "a[routerlink='performance']")
    expances = (By.CSS_SELECTOR, "a[routerlink='expenses']")
    apps = (By.CSS_SELECTOR, "a[routerlink='apps']")

    def __init__(self, driver):
        self.driver = driver

    def clickonMefunction(self):
        self.driver.find_element(*self.me_function).click()

    def clickonleave(self):
        self.driver.find_element(*self.leave).click()

    def clickonattendence(self):
        self.driver.find_element(*self.attendence).click()

    def clickonperformance(self):
        self.driver.find_element(*self.performance).click()

    def clickonexpances(self):
        self.driver.find_element(*self.expances).click()

    def clickonapps(self):
        self.driver.find_element(*self.apps).click()
