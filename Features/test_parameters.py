import math

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

@pytest.mark.parametrize("num1,num2,expected_result",(["25","12","37"],[12,13,"25"]))
def test_parameterize(num1,num2,expected_result):
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    driver.find_element(By.ID,"sum1").send_keys(num1)
    driver.find_element(By.ID,"sum2").send_keys(num2)
    driver.find_element(By.XPATH,"//button[normalize-space()='Get Sum']").click()
    actual_result = driver.find_element(By.XPATH,"//p[@id='addmessage']").text
    assert actual_result==expected_result,"expected result does not match with the actual"

#Parameterise with two decorators
@pytest.mark.parametrize("base",[1,2,3])
@pytest.mark.parametrize("exponent",[2,4,6])
def test_two_parameters(base,exponent):
    result = base ** exponent
    assert result == math.pow(base,exponent)