from selenium.webdriver.common.by import By

def test_create_folder(browser):
    folder_name = "TestFolder"
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()

    browser.find_element(By.ID, "name").send_keys(folder_name)
    browser.find_element(By.CLASS_NAME, "com_cloudbees_hudson_plugins_folder_Folder").click()
    browser.find_element(By.ID, "ok-button").click()

    browser.find_element(By.NAME, "Submit").click()

    assert f"/job/{folder_name}/" in browser.current_url
    assert browser.find_element(By.CLASS_NAME, "job-index-headline").text == folder_name
