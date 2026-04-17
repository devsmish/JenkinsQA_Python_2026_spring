from selenium import webdriver
from selenium.webdriver.common.by import By


def test_input_username(browser):
    text = "Login"

    browser.get("http://localhost:8080/login?from=%2F")

    browser.implicitly_wait(0.5)

    text_area = browser.find_element(by=By.NAME, value="j_username")

    text_area.send_keys(text)

    assert text_area.get_attribute("value") == "Login"
