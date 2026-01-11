from selenium import webdriver
import allure
import pytest

@allure.title("commands")
def test_basic_commands():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://thetestingacademy.com/")
    print(driver.title)
    print(driver.current_url)

    driver.quit()
