
from selenium import webdriver

def test_open_site():
    driver = webdriver.Chrome()
    driver.get("https://www.python.org")

    assert "Python" in driver.title


    driver.quit()