import string
import random
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def sign_in(browser):
    browser.get("http://localhost:8080/")
    browser.find_element(By.XPATH, "//*[@id='j_username']").send_keys("admin")
    browser.find_element(By.XPATH, "//*[@id='j_password']").send_keys("admin")
    browser.find_element(By.XPATH, "//*[@id='main-panel']/div/form/button").click()


def test_exercise(browser):
    sign_in(browser)

    excepted_name = browser.find_element(By.XPATH, "//*[@id='main-panel']/div[2]/div/h1").text
    assert excepted_name == "Welcome to Jenkins!"







