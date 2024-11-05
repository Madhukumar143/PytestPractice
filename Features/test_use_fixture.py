import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

@pytest.fixture()
def setup_teardown():
    driver.get("https://ecommerce-playground.lambdatest.io/")
    driver.find_element(By.XPATH,"(//span[normalize-space()='My account'])[2]").click()
    hover_element = driver.find_element(By.XPATH,"(//span[normalize-space()='My account'])[2]")
    actions = ActionChains(driver)
    actions.move_to_element(hover_element).perform()
    driver.find_element(By.XPATH,"//span[normalize-space()='Login']").click()
    driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys("madhukumarhm123.com@gmail.com")
    driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("Test@3442")
    driver.find_element(By.XPATH,"//input[@value='Login']").click()
    print("Login")
    yield
    driver.find_element(By.LINK_TEXT,"Logout").click()

@pytest.fixture()
def setup_and_teardown():
    driver.get("https://awesomeqa.com/ui/")
    time.sleep(3)

@pytest.mark.usefixtures("setup_and_teardown")
def test_order_history_title():
    driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("hp")
    driver.find_element(By.XPATH,"//span[@class='input-group-btn']").click()
    assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed(),"search results not found"
    verification_text = ""

@pytest.mark.usefixtures("setup_teardown")
def test_change_password():
    driver.find_element(By.LINK_TEXT,"Password").click()
    driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("Test@3442")
    driver.find_element(By.XPATH,"//input[@id='input-confirm']").send_keys("Test@3442")
    driver.find_element(By.XPATH,"//input[@value='Continue']").click()
    confirmation_text = "Success: Your password has been successfully updated."
    after_changing = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
    assert confirmation_text.__contains__(after_changing), "password not changed"


