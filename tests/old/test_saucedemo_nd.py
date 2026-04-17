import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--incognito")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_login(driver):
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    logout_button = wait.until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
    assert logout_button.is_displayed()

def test_confirm_product_title(driver):
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    driver.find_element(By.XPATH, "//div[contains(text(), 'Sauce Labs Fleece Jacket')]").click()
    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Sauce Labs Fleece Jacket')]")))
    assert element.text == 'Sauce Labs Fleece Jacket'