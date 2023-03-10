from lib.login import Loginpage
from lib.mefunction import MeFunctionality
from data import config


class TestMefunction():
    url = config.base_url
    user = config.username
    password = config.password

    def test_mefunctionality(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        self.logs = Loginpage(self.driver)
        self.logs.clickonpassword()
        self.logs.set_username(self.user)
        self.logs.set_password(self.password)
        self.logs.clickonlogin()
        self.target = MeFunctionality(self.driver)
        self.target.clickonMefunction()
        self.target.clickonleave()
        self.target.clickonattendence()
        self.target.clickonperformance()
        self.target.clickonexpances()
        # self.target.clickonapps()
        actual_title = self.driver.title
        print(actual_title)
        if actual_title == " Me | Expenses |Pending":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("..\\screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
