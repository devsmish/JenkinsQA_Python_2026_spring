import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://www.selenium.dev/selenium/web/web-form.html"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()

def test_password_field_max_lenght(browser):
    browser.get(URL)
    password_field = browser.find_element(By.CSS_SELECTOR, "input[name='my-password']")
    time.sleep(3)
    maxlenght = password_field.get_attribute("maxlength")

    assert maxlenght is None

    long_password = 'a'*100
    time.sleep(3)
    password_field.send_keys(long_password)
    entered_value = password_field.get_attribute("value")
    time.sleep(3)
    assert len(entered_value) == 100
