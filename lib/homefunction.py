from selenium import webdriver
from selenium.webdriver.common.by import By
from data import config


url = config.base_url
user = config.username
password = config.password


class Homefunctionality():

    Home_function = (By.XPATH, "//span[normalize-space()='Home']")
    holidays_element = (
         By.CSS_SELECTOR, "div[class='d-flex align-items-center justify-content-between'] a[class='text-white']")
    close_button = (By.XPATH, "//span[@class='ic-close icon icon-sm']")
    Birth_ele = (By.XPATH, "//span[@class='icon ic-cake icon-xxs icon-accent-red']")
    work_ele = (By.XPATH, "//span[@class='dot dot-md-lg bg-accent-green-light align-self-center']")
    # newjoin_ele = (By.XPATH, "//span[@class='icon ic-supervisor icon-xxs icon-accent-violet']")
    newjoin_ele = (By.CSS_SELECTOR, ".icon.ic-supervisor.icon-xxs.icon-accent-violet")

    def __init__(self, driver):
        self.driver = driver

    def click_homefunction(self):
        self.driver.find_element(*self.Home_function).click()

    # def clickonHolidays(self):
        # self.driver.implicitly_wait(5)
        # self.driver.find_element(*self.holidays_element).click()
        # self.driver.find_element(*self.close_button).click()

    def clickonBirthdays(self):
        self.driver.find_element(*self.Birth_ele).click()

    def clickonworkanniversarys(self):
        self.driver.find_element(*self.work_ele).click()

    def clickonnewjoiners(self):
        self.driver.find_element(*self.newjoin_ele).click()
