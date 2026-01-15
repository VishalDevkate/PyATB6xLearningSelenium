from selenium import webdriver
import allure
import pytest


@allure.title("Verify tile in firefox driver")
def test_third_tc():
    # Selenium 4
    driver = webdriver.Firefox()
    driver.get("https://thetestingacademy.com")
    print(driver.title)
    assert driver.title == "TheTestingAcademy | Learn Software Testing and Automation Testing"

    driver.quit()