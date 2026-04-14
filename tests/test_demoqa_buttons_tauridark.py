import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

button_url = "https://demoqa.com/buttons"

def test_button_double_click(browser):
    """
    Successful click on button 'Double Click Me'
    """

    browser.get(button_url)
    button_double_click = browser.find_element(
        By.XPATH, "//button[@id='doubleClickBtn']"
    )

    time.sleep(1)
    ActionChains(browser).double_click(button_double_click).perform()

    appeared_element = browser.find_element(By.XPATH, "//p[@id='doubleClickMessage']")

    assert appeared_element.text == "You have done a double click"


def test_button_right_click(browser):
    """
    Successful click on button 'Right Click Me'
    """

    browser.get(button_url)
    button_right_click = browser.find_element(
        By.XPATH, "//button[@id='rightClickBtn']"
    )

    time.sleep(1)
    ActionChains(browser).context_click(button_right_click).perform()

    appeared_element = browser.find_element(By.XPATH, "//p[@id='rightClickMessage']")

    assert appeared_element.text == "You have done a right click"

def test_button_click(browser):
    """
    Successful click on button 'Click Me'
    """

    browser.get(button_url)
    button_click = browser.find_element(
        By.XPATH, "//button[text()='Click Me']"
    )
    time.sleep(1)
    button_click.click()

    appeared_element = browser.find_element(By.XPATH, "//p[@id='dynamicClickMessage']")

    assert appeared_element.text == "You have done a dynamic click"
