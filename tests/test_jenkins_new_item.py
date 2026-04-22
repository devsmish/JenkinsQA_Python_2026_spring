from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_new_item_is_available(browser):
    """ Находим кнопку 'New Item' """
    wait = WebDriverWait(browser, 10)
    new_item_button = wait.until(
        EC.visibility_of_element_located((By.LINK_TEXT, "New Item"))
    )

    assert new_item_button.is_displayed()


def test_signin_page_header_exists(browser):
    """
    Проверяем, что пользователь видит страницу входа (Sign in).
    """
    base_url = "http://localhost:8081"
    browser.get(f"{base_url}/logout")
    browser.get(base_url)

    assert "Sign in - Jenkins" in browser.title
