from selenium.webdriver.common.by import By

def test_validate_empty_item_name(browser):
    """Тест на валидацию пустого поля Item Name"""
    new_item = browser.find_element(By.CSS_SELECTOR, ".task-link.task-link-no-confirm ")
    new_item.click()
    folder_radio = browser.find_element(By.CLASS_NAME, "com_cloudbees_hudson_plugins_folder_Folder")
    folder_radio.click()

    validation_message = browser.find_element(By.ID, "itemname-required")
    assert validation_message.text == "» This field cannot be empty, please enter a valid name"