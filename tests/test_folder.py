from selenium.webdriver.common.by import By

FOLDER_NAME = "TestFolder"


def test_create_folder(browser):
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()

    browser.find_element(By.ID, "name").send_keys(FOLDER_NAME)
    browser.find_element(By.CLASS_NAME, "com_cloudbees_hudson_plugins_folder_Folder").click()
    browser.find_element(By.ID, "ok-button").click()

    browser.find_element(By.NAME, "Submit").click()

    assert f"/job/{FOLDER_NAME}/" in browser.current_url
    assert browser.find_element(By.CLASS_NAME, "job-index-headline").text == FOLDER_NAME


def test_create_folder_with_display_name(browser):
    display_name = "Display Folder"

    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()

    browser.find_element(By.ID, "name").send_keys(FOLDER_NAME)
    browser.find_element(By.CLASS_NAME, "com_cloudbees_hudson_plugins_folder_Folder").click()
    browser.find_element(By.ID, "ok-button").click()

    browser.find_element(By.NAME, "_.displayNameOrNull").send_keys(display_name)
    browser.find_element(By.NAME, "Submit").click()

    assert browser.find_element(By.CLASS_NAME, "job-index-headline").text == display_name
    folder_name_line = \
        [line for line in browser.find_element(By.ID, "main-panel").text.split('\n') if
         line.startswith("Folder name: ")][0]
    assert folder_name_line == f"Folder name: {FOLDER_NAME}"

def test_create_folder_with_description(browser):
    description = "Description"

    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()

    browser.find_element(By.ID, "name").send_keys(FOLDER_NAME)
    browser.find_element(By.CLASS_NAME, "com_cloudbees_hudson_plugins_folder_Folder").click()
    browser.find_element(By.ID, "ok-button").click()

    browser.find_element(By.NAME, "_.description").send_keys(description)
    browser.find_element(By.NAME, "Submit").click()
    assert browser.find_element(By.ID, "view-message").text == description

def test_create_nested_folder(browser):
    nested_folder = "NestedFolder"
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()

    browser.find_element(By.ID, "name").send_keys(FOLDER_NAME)
    browser.find_element(By.CLASS_NAME, "com_cloudbees_hudson_plugins_folder_Folder").click()
    browser.find_element(By.ID, "ok-button").click()

    browser.find_element(By.NAME, "Submit").click()

    # создаем вложенную папку
    browser.find_element(By.XPATH, f"//a[@href='/job/{FOLDER_NAME}/newJob']").click()

    browser.find_element(By.ID, "name").send_keys(nested_folder)
    browser.find_element(By.CLASS_NAME, "com_cloudbees_hudson_plugins_folder_Folder").click()
    browser.find_element(By.ID, "ok-button").click()

    browser.find_element(By.NAME, "Submit").click()

    assert f"/job/{FOLDER_NAME}/job/{nested_folder}/" in browser.current_url
    assert browser.find_element(By.CLASS_NAME, "job-index-headline").text == nested_folder
    full_folder_name_line = \
        [line for line in browser.find_element(By.ID, "main-panel").text.split('\n') if
         line.startswith("Full folder name: ")][0]
    assert full_folder_name_line == f"Full folder name: {FOLDER_NAME}/{nested_folder}"
    breadcrumb_texts = [
        crumb.text for crumb in browser.find_elements(By.CSS_SELECTOR, ".jenkins-breadcrumbs__list-item")
    ]
    assert breadcrumb_texts == [FOLDER_NAME, nested_folder]