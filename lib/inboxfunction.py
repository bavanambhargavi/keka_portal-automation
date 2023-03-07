from selenium.webdriver.common.by import By
from data import config


url = config.base_url
user = config.username
password = config.password


class InboxFunctionality():
    Inbox_locat = (By.XPATH, "//span[normalize-space()='Inbox']")
    takeact_loc = (By.CSS_SELECTOR, "a[routerlink='action']")
    Notification_loc = (By.XPATH, "//a[normalize-space()='Notifications']")

    def __init__(self, driver):
        self.driver = driver

    def checkonInbox(self):
        self.driver.find_element(*self.Inbox_locat).click()
        self.driver.find_element(*self.takeact_loc).click()
        self.driver.find_element(*self.Notification_loc).click()
