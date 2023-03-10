import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver


# def pytest_addoption(parser):
#     parser.addoption("--browser")


# @pytest.fixture
# def brow(request):
#     return request.config.getoption("--browser")
