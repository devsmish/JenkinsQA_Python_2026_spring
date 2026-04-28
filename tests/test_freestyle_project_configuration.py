from selenium.webdriver.common.by import By


def create_freestyle_project(driver):

    driver.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    driver.find_element(By.ID, "name").send_keys('Test')
    driver.find_element(By.CSS_SELECTOR, "li.hudson_model_FreeStyleProject").click()
    driver.find_element(By.XPATH, '//*[@id="ok-button"]').click()
    driver.find_element(By.NAME, "Submit").click()


def test_disable_active_project(browser):
    create_freestyle_project(browser)

    browser.find_element(By.ID, 'jenkins-head-icon').click()

    browser.find_element(By.CSS_SELECTOR, 'button.jenkins-menu-dropdown-chevron').click()
    browser.find_element(By.XPATH, "//a[contains(@href, 'configure')]").click()

    browser.find_element(By.CSS_SELECTOR, 'label[for="enable-disable-project"]').click()
    browser.find_element(By.NAME, "Submit").click()

    assert browser.find_element(
        By.XPATH, "//*[contains(text(), 'This project is currently disabled')]"
    )