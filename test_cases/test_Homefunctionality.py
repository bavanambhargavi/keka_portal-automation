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
        
        self.home.clickonBirthdays()
        self.home.clickonworkanniversarys()
    
        self.home.clickonnewjoiners()
