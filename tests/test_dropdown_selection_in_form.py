from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dropdown_selection_in_form(browser):
    """
    Проверка создания формы с выбранным значением "Two" в поле Dropdown (select)
    """
    browser.get("https://www.selenium.dev/selenium/web/web-form.html")

    dropdown_select = browser.find_element(By.NAME, "my-select")
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

    select = Select(dropdown_select)

    available_options = [opt.text for opt in select.options]
    assert "Two" in available_options, f"В списке отсутствует 'Two'. Список содержит: {available_options}"

    select.select_by_visible_text("Two")

    select_option = select.first_selected_option
    assert select_option.text == "Two", f"Ошибка: выбрано {select_option.text},а должно 'Two'"

    button.click()

    message = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "message")))
    assert message.text == "Received!", f"Ошибка, форма не отправилась"
