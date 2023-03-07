import time
from data import config
from lib.homefunction import Homefunctionality
from lib.login import Loginpage


class TestHomeFunction():

    url = config.base_url
    user = config.username
    password = config.password

    def test_Homefunction(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.log = Loginpage(self.driver)
        self.log.clickonpassword()
        self.log.set_username(self.user)
        self.log.set_password(self.password)
        self.log.clickonlogin()

        self.home = Homefunctionality(self.driver)
        self.home.click_homefunction()
        # self.home.clickonHolidays()
        time.sleep(3)
        self.home.clickonBirthdays()
        self.home.clickonworkanniversarys()
        time.sleep(4)
        self.home.clickonnewjoiners()
