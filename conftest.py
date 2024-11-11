import pytest
from selenium import webdriver


@pytest.fixture(params = ["chrome","edge"])
def initialize_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "edge":
        driver = webdriver.Edge()
    request.cls.driver = driver
    print("Browser : ",request.param)
    yield
    print("Close driver")
    driver.close()