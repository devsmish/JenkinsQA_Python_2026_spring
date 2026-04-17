import time
from selenium.webdriver.common.by import By

def test_delete_checkbox(browser):
    browser.get("https://the-internet.herokuapp.com/checkboxes")
    checkbox2 = browser.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(3)")
    assert checkbox2.is_selected()
    time.sleep(4)
    checkbox2.click()
    time.sleep(4)
    assert not checkbox2.is_selected()