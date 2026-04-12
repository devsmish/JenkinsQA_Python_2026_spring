from selenium.webdriver.common.by import By

UNAME = (By.XPATH, '//*[@id="loginPanel"]/form/div[1]/input')
PWD = (By.XPATH,'//*[@id="loginPanel"]/form/div[2]/input')
BTN = (By.XPATH,'//*[@id="loginPanel"]/form/div[3]/input')


def test_input_admin(browser):
    """Негативный тест логина в админ-панель"""
    browser.implicitly_wait(2)
    browser.get("https://parabank.parasoft.com/parabank/admin.htm")

    text_box1 = browser.find_element(*UNAME)
    text_box2 = browser.find_element(*PWD)
    submit_button = browser.find_element(*BTN)

    text_box1.send_keys("Selenium")
    text_box2.send_keys("Test")
    submit_button.click()

    element = browser.find_element(By.CSS_SELECTOR, "#rightPanel > p")
    text = element.text
    print('\n', text)

    assert "could not be verified" in text