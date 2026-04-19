from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

multiconfiguration_project_name = "MultiConfig_Name"

def test_verify_status_switching_enable_button(browser):
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()

    browser.find_element(By.ID, "name").send_keys(multiconfiguration_project_name)
    browser.find_element(By.CLASS_NAME, "hudson_matrix_MatrixProject").click()
    browser.find_element(By.ID, "ok-button").click()
    browser.find_element(By.NAME, "Submit").click()

    browser.find_element(By.XPATH, "//a[@href='/job/" + multiconfiguration_project_name + "/configure']").click()
    browser.find_element(By.CSS_SELECTOR, "#toggle-switch-enable-disable-project > label").click()
    browser.find_element(By.NAME, "Submit").click()

    actual_disable_text = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "enable-project"))).text

    assert "This project is currently disabled" in actual_disable_text
