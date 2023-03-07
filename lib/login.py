from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from data import config

url = config.base_url
user = config.username
password = config.password


class Loginpage:
    locat = (By.XPATH, "//p[normalize-space()='Keka Password']")
    USERNAME = (By.XPATH, "//input[@id='email']")
    PASWORRD = (By.CSS_SELECTOR, "#password")
    Login_button = (By.XPATH, "//button[normalize-space()='Login']")

    def __init__(self, driver):
        self.driver = driver

    def clickonpassword(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.locat).click()

    def set_username(self, user):
        self.driver.find_element(*self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(user)

    def set_password(self, password):
        self.driver.find_element(*self.PASWORRD).clear()
        self.driver.find_element(*self.PASWORRD).send_keys(password)

    def clickonlogin(self):
        self.driver.find_element(*self.Login_button).click()
