from lib.orgfunction import OrgFunction
from lib.login import Loginpage
from data import config
import time


class TestOrginazation():

    url = config.base_url
    user = config.username
    password = config.password

    def test_check_orginzation(self, driver):
        self.driver = setup
        self.driver.get(self.url)
        self.log = Loginpage(self.driver)
        self.log.clickonpassword()
        self.log.set_username(self.user)
        self.log.set_password(self.password)
        self.log.clickonlogin()
        self.org = OrgFunction(self.driver)
        self.org.clickonorg()
        

        
