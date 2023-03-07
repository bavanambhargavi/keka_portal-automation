import pytest 
from selenium import webdriver


@pytest.fixture(scope="function")
def setup():
    # print(brow)
    # brow == "chrome"
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.close()


# def pytest_addoption(parser):
#     parser.addoption("--browser")


# @pytest.fixture
# def brow(request):
#     return request.config.getoption("--browser")

