from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_kirill_input():
    param_word = "123456"
    driver = webdriver.Chrome()

    driver.get("https://www.selenium.dev/selenium/web/inputs.html")

    time.sleep(2)

    number_input = driver.find_element(By.NAME, "number_input")

    number_input.send_keys(param_word)

    submit_button = driver.find_element(By.NAME, "submit_input")

    submit_button.click()

    time.sleep(2)
    current_url = driver.current_url

    assert param_word in current_url





