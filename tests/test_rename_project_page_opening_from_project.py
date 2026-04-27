import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def create_new_freestyle_project(browser):
    wait = WebDriverWait(browser, 5)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/view/all/newJob']"))).click()
    project_name = f"test_project_{int(time.time())}"
    wait.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys(project_name)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Freestyle project')]"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()
    wait.until(EC.presence_of_element_located((By.NAME, "Submit")))
    wait.until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()
    return project_name

def test_rename_freestyle_project_from_project_page(browser):
    project_name = create_new_freestyle_project(browser)
    rename = browser.find_element(By.PARTIAL_LINK_TEXT, 'Rename')
    rename.click()
    rename_page_title = browser.find_element(By.TAG_NAME, 'h1')
    assert rename_page_title.text == f'Rename Project {project_name}'




