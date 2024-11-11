import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By




@pytest.mark.usefixtures("initialize_driver")
class baseclass:
    pass

class Test_Drivers(baseclass):

    def test_multiple_browsers(self):
        self.driver.get("https://www.lambdatest.com/selenium-playground/")
        header = self.driver.find_element(By.XPATH,"//section[@class='sp__main']//div//h1").text
        print("Header : ", header)
        assert header == "Selenium Playground", "header is not matching"





