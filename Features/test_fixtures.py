import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

@pytest.fixture(autouse = True)
def automatic_fixture():
    print("Automatic fixture")

@pytest.fixture(scope="module") #by default it will be for every function
def setup_teardown():
    driver.get("https://ecommerce-playground.lambdatest.io/")
    driver.find_element(By.XPATH,"(//span[normalize-space()='My account'])[2]").click()
    hover_element = driver.find_element(By.XPATH,"(//span[normalize-space()='My account'])[2]")
    actions = ActionChains(driver)
    actions.move_to_element(hover_element).perform()
    driver.find_element(By.XPATH,"//span[normalize-space()='Login']").click()
    driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys("madhukumarhm123.com@gmail.com")
    driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("Test@3442")
    driver.find_element (By.XPATH,"//input[@value='Login']").click()
    print("Login")
    yield
    driver.find_element(By.LINK_TEXT,"Logout").click()
    print("logout")

def test_order_history_title(setup_teardown):
    print("verifying order history page title")
    actual_title = "Order History"
    driver.find_element(By.XPATH,"//a[normalize-space()='Order History']").click()
    assert driver.title==actual_title,"title does not match test failed"


def test_change_password(setup_teardown):
    print("changing the password")
    driver.find_element(By.LINK_TEXT,"Password").click()
    driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("Test@3442")
    driver.find_element(By.XPATH,"//input[@id='input-confirm']").send_keys("Test@3442")
    driver.find_element(By.XPATH,"//input[@value='Continue']").click()
    confirmation_text = "Success: Your password has been successfully updated."
    after_changing = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
    assert confirmation_text.__contains__(after_changing), "password not changed"


