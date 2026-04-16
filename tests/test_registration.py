import string
import random
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CONFIRM_BUTTON = "((//div[@class='fc-footer-buttons'])[1]//p)[1]"
SIGNUP_BUTTON = "//a[contains(text(), ' Signup / Login')]"
LOGOUT_BUTTON = "//a[contains(text(), ' Logout')]"

@pytest.fixture
def get_wait3(browser):
    return WebDriverWait(browser, 3)

def test_registration(browser, get_wait3):

    chars = string.ascii_letters + string.digits
    random_email = "".join(random.choice(chars) for _ in range(10)) + "@Joba.com"

    browser.get("https://automationexercise.com/")
    get_wait3.until(
        EC.element_to_be_clickable((By.XPATH, CONFIRM_BUTTON))).click()
    get_wait3.until(
        EC.element_to_be_clickable((By.XPATH, SIGNUP_BUTTON))).click()

    get_wait3.until(
        EC.visibility_of_element_located((By.XPATH, "//input[@data-qa='signup-name']"))).send_keys("testUser")
    browser.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(random_email)
    browser.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

    get_wait3.until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='id_gender1']"))).click()
    browser.find_element(By.XPATH, "//input[@id='password']").send_keys("testPassword")
    browser.find_element(By.XPATH, "//input[@id='first_name']").send_keys("testFirstName")
    browser.find_element(By.XPATH, "//input[@id='last_name']").send_keys("testLastName")
    browser.find_element(By.XPATH, "//input[@id='address1']").send_keys("Street Kolotushkina")
    browser.find_element(By.XPATH, "//select[@id='country']").click()
    get_wait3.until(
        EC.element_to_be_clickable((By.XPATH, "//option[@value='Israel']"))).click()
    browser.find_element(By.XPATH, "//input[@id='state']").send_keys("Tegeran")
    browser.find_element(By.XPATH, "//input[@id='city']").send_keys("Bangladesh")
    browser.find_element(By.XPATH, "//input[@id='zipcode']").send_keys("777777")
    browser.find_element(By.XPATH, "//input[@id='mobile_number']").send_keys("88005553535")

    browser.find_element(By.XPATH, "//button[@data-qa='create-account']").click()

    assert get_wait3.until(EC.visibility_of_element_located((By.XPATH, "//h2[@data-qa='account-created']"))).text == "ACCOUNT CREATED!"
    return random_email

def test_email_that_already_exists(browser, get_wait3):

    random_email = test_registration(browser, get_wait3)

    browser.get("https://automationexercise.com/")
    get_wait3.until(
        EC.element_to_be_clickable((By.XPATH, LOGOUT_BUTTON))
    ).click()
    get_wait3.until(
        EC.element_to_be_clickable((By.XPATH, SIGNUP_BUTTON))
    ).click()

    get_wait3.until(
        EC.visibility_of_element_located((By.XPATH, "//input[@data-qa='signup-name']"))).send_keys("testUser")
    browser.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(random_email)
    browser.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

    assert get_wait3.until(EC.visibility_of_element_located((By.XPATH, "//form[@action='/signup']/p"))).text == "Email Address already exist!"