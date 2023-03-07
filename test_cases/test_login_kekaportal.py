from data import config
from lib.login import Loginpage


class TestLogin():
    url = config.base_url
    user = config.username
    password = config.password

    def test_keka_login(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.source = Loginpage(self.driver)
        self.source.clickonpassword()
        self.source.set_username(self.user)
        self.source.set_password(self.password)
        self.source.clickonlogin()
        

