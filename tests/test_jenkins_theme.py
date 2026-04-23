from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_new_theme_dropdown(browser):
    # Шаг 1. Находим профиль и наводим курсор
    profile_element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root-action-UserAction']"))
    )
    actions = ActionChains(browser)
    actions.move_to_element(profile_element).perform()

    import time
    time.sleep(1)

    # Шаг 2. Ждем появления пункта "Theme" и кликаем по нему
    select_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@id='account-theme-picker']"))
    )
    select_element.click()

    # Шаг 3. Ждем появления select с темами
    theme_select = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='account-theme-picker']"))
    )

    # Шаг 4. Выбираем тему
    dark_theme = theme_select.find_element(By.XPATH, "//option[@value='dark']")
    dark_theme.click()

    time.sleep(15)

