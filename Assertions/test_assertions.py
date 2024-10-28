import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.smoke
def test_assertions():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
    driver.find_element(By.XPATH,"//h4[normalize-space()='Gender :']/following::input[@value='Female']").click()
    driver.find_element(By.XPATH,"//input[@value='5 - 15']").click()
    driver.find_element(By.XPATH,"//button[normalize-space()='Get values']").click()
    gender_selected = driver.find_element(By.CSS_SELECTOR,".genderbutton").text
    age_group_selected = driver.find_element(By.CSS_SELECTOR,".groupradiobutton").text
    # here == will compare the values even though ids are different
    """assert gender_selected == "Female", "Female option is not selected"
    print("id of gender_selected : ", id(gender_selected))
    print("id of Male : ", id("Female"))
    # here we used is, it is considering age group selected and "5 - 15" as two different objects
    print("id of age_group_selected :",id(age_group_selected))
    print("id of 5 - 15 : ",id("5 - 15"))
    assert age_group_selected == "5 - 15", "5 - 15 option is not selected"""
    #validate the title
    title = driver.title
    assert title.__contains__("Selenium Grid Online"), "title is not matching"

@pytest.mark.regression
def test_two():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
    print("test two")
    driver.find_element(By.XPATH,"//h4[normalize-space()='Gender :']/following::input[@value='Female']").click()
    driver.find_element(By.XPATH,"//input[@value='5 - 15']").click()
    driver.find_element(By.XPATH,"//button[normalize-space()='Get values']").click()
    title = driver.title
    assert title.__contains__("Selenium Grid Online"), "title is not matching"

@pytest.mark.sanity
def test_login():
    print("login")

@pytest.mark.sanity
def test_logout():
    print("logout")