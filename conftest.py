import pytest 
from selenium import webdriver


@pytest.fixture()
def setup():
    print()
    # brow =s= "chrome"
    # global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.close()


# def pytest_addoption(parser):
#     parser.addoption("--browser")


# @pytest.fixture
# def brow(request):
#     return request.config.getoption("--browser")

