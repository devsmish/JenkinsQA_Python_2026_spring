import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_with_try_finally(driver):

    try:

        driver.get("https://the-internet.herokuapp.com/login")
        print("✓ Страница логина открыта")


        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username_field.send_keys("tomsmith")


        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("SuperSecretPassword!")


        login_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )
        login_button.click()


        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "flash.success"))
        )

        assert "You logged into a secure area!" in success_message.text
        print(f"✓ Успешный вход: {success_message.text}")

    except Exception as e:
        print(f"✗ Ошибка во время теста: {e}")
        raise
    finally:

        print("Завершение теста — закрытие браузера")