from selenium import webdriver
import allure
import pytest

@allure.title("Print page source and verify text present on page")
def test_second_tc():
    driver = webdriver.Chrome()
def test_tc1():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    print("Page Title: ", driver.title)
    print("current Page URL: ", driver.current_url)
    print("Page Source: ", driver.page_source)
    assert "CURA Healthcare Service" in driver.page_source

    driver.quit()
