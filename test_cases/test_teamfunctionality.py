from lib.myteamfunction import MyTeam
from lib.login import Loginpage
from data import config


class TestMyteam():

    url = config.base_url
    user = config.username
    password = config.password

    def test_teamfun(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.log = Loginpage(self.driver)
        self.log.clickonpassword()
        self.log.set_username(self.user)
        self.log.set_password(self.password)
        self.log.clickonlogin()
        self.team = MyTeam(self.driver)
        self.team.myteam()
    
