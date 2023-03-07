from selenium.webdriver.common.by import By
from data import config


url = config.base_url
user = config.username
password = config.password


class OrgFunction():
    org_l = (By.XPATH, "//span[@class='ic-org sidebar-list-icon']")
    # employee = (By.XPATH, "//span[normalize-space()='Employees']")
    Doc = (By.XPATH, "//li[@class='active']//a[normalize-space()='Documents']")
    engage_loc = (By.XPATH, "//a[@routerlink='engage']")

    def __init__(self, driver):
        self.driver = driver

    def clickonorg(self):
        self.driver.find_element(*self.org_l).click()
        # self.driver.find_element(*self.employee).click()
        self.driver.find_element(*self.Doc).click()
        self.driver.find_element(*self.engage_loc).click()


