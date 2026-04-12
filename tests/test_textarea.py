from selenium import webdriver
from selenium.webdriver.common.by import By


def test_textarea(browser):
    text = "New text"

    browser.get("https://www.selenium.dev/selenium/web/web-form.html")

    browser.implicitly_wait(0.5)

    text_box = browser.find_element(by=By.NAME, value="my-textarea")

    text_box.send_keys(text)

    assert text_box.get_attribute("value") == "New text"