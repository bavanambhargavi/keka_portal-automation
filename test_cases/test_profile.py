from lib.profile import Profilpage
from lib.login import Loginpage
from data import config


class TestProfileTab():

    url = config.base_url
    user = config.username
    password = config.password

    def test_check_profile(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        self.log = Loginpage(self.driver)
        self.log.clickonpassword()
        self.log.set_username(self.user)
        self.log.set_password(self.password)
        self.log.clickonlogin()
        self.profile = Profilpage(self.driver)
        self.profile.clickondown()
        self.profile.checkprofile()
        self.profile.clickonpassword()
        self.profile.changepassword()

