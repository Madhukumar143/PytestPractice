import time
import softest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Assertions(softest.TestCase):

    def test_assertions(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
        driver.find_element(By.XPATH,"//h4[normalize-space()='Gender :']/following::input[@value='Male']").click()
        driver.find_element(By.XPATH,"//input[@value='5 - 15']").click()
        driver.find_element(By.XPATH,"//button[normalize-space()='Get values']").click()
        gender_selected = driver.find_element(By.CSS_SELECTOR,".genderbutton").text
        age_group_selected = driver.find_element(By.CSS_SELECTOR,".groupradiobutton").text
        # here == will compare the values even though ids are different
        self.soft_assert(self.assertEqual,"Female",gender_selected,"gender selected is not correct")
        print("Test hello")
        self.soft_assert(self.assertEqual,"15 - 15",age_group_selected,"age group selected is not correct")
        self.soft_assert(self.assertTrue,driver.title.__contains__("Selenium Grid Online"),"title does not match")
        self.assert_all("verify Gender, Age_group & title")
