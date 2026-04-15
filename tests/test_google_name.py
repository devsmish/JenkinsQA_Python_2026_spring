import time
from selenium import webdriver


def test_1():
    browser = webdriver.Chrome()
    browser.get("https://www.google.com/")

    time.sleep(3)

    title = browser.title

    assert 'Google' in title
    browser.quit()