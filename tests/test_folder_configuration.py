import pytest
from selenium.webdriver.common.by import By

from test_folder import create_folder

FOLDER_NAME = "TestFolder"
DISPLAY_NAME = "Display Folder"


@pytest.mark.dependency()
def test_add_display_name_to_folder(browser):
    create_folder(browser, FOLDER_NAME)
    browser.find_element(By.XPATH, "//a[contains(@href, '/configure')]").click()

    browser.find_element(By.NAME, "_.displayNameOrNull").send_keys(DISPLAY_NAME)
    browser.find_element(By.NAME, "Submit").click()

    assert browser.find_element(By.CLASS_NAME, "job-index-headline").text == DISPLAY_NAME
    folder_name_line = \
        [line for line in browser.find_element(By.ID, "main-panel").text.split('\n') if
         line.startswith("Folder name: ")][0]
    assert folder_name_line == f"Folder name: {FOLDER_NAME}"
