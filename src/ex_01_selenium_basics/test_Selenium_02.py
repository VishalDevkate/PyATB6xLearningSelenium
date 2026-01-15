from selenium import webdriver
import allure
import pytest

@allure.title("second test case(Edge browser): open page using selenium and verify expected title")
@allure.description("open page using selenium and verify expected title")
def test_second_tc():
    # Selenium 3 - Not much used now
    # driver_path = '/Users/pramod/Downloads/edge/msedgedriver'
    # driver = webdriver.EdgeService(executable_path=driver_path)
    # Selenium 4 code below
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://thetestingacademy.com/")
    assert driver.title == "TheTestingAcademy | Learn Software Testing and Automation Testing"

    driver.quit()
