from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from data import config

url = config.base_url
user = config.username
password = config.password


class Profilpage():
    move_down = (By.XPATH,  "//span[@class='ic-move-down icon']")
    profile = (By.XPATH, "//a[normalize-space()='Profile']")
    change_password = (By.XPATH, "//a[normalize-space()='Change Password']")
    # change_password = (By.XPATH, '//*[@id="top-nav"]/div/div/a[2]')
    curr_password = (By.ID, "currentPassword")
    new_pass = (By.CSS_SELECTOR, "#newPassword")
    confirm_pass = (By.ID, "confirmPassword")
    change_password = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def clickondown(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.move_down).click()

    def checkprofile(self):
        self.driver.find_element(*self.profile).click()

    def clickonpassword(self):
        self.driver.find_element(*self.change_password).click()
        self.driver.find_element(*self.curr_pasword).send_keys("Abhiram@44")

    def changepassword(self):
        self.driver.find_element(*self.new_pass).send_keys("Bhargavi@97")
        self.driver.find_element(*self.confirm_pass).send_keys("Bhargavi@97")
        self.driver.find_element(*self.change_password).click()
