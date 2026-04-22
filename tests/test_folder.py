from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

def test_create_new_folder(browser):
    name = "new_folder"
    
    wait = WebDriverWait(browser, 2)
    browser.find_element(By.XPATH, "//*[@id='tasks']/div[1]/span/a").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='add-item-panel']/h1")))
    browser.find_element(By.ID, "name").send_keys("new_folder")
    browser.find_element(By.XPATH, "//*[@id='j-add-item-type-nested-projects']/ul/li[1]").click()
    browser.find_element(By.XPATH, "//*[@id='ok-button']").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='bottom-sticker']/div/button[1]")))
    browser.find_element(By.XPATH, "//*[@id='bottom-sticker']/div/button[1]").click()

    assert name == browser.find_element(By.XPATH, "//*[@id='main-panel']/div[1]/div/h1").text
