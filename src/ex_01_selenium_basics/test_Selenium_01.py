from selenium import webdriver
import allure
import pytest

@allure.title("first test case: open page using selenium and verify expected title")
@allure.description("open page using selenium and verify expected title")
def test_first_tc():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://thetestingacademy.com/")
    assert driver.title == "TheTestingAcademy | Learn Software Testing and Automation Testing"

    driver.quit()
