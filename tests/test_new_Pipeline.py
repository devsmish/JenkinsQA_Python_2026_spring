import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_new_Pipeline(browser):
    browser.find_element(By.LINK_TEXT, "New Item").click()
    browser.find_element(By.ID, "name").send_keys("test_1")

    browser.find_element(By.XPATH,"//ul/li//span[text()='Pipeline']").click()
    browser.find_element(By.ID, "ok-button").click()

    wait = WebDriverWait(browser, 10)
    wait.until(EC.element_to_be_clickable((By.NAME,"Submit"))).click()

    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='app-jenkins-logo']"))).click()

    wait = WebDriverWait(browser, 10)
    label=wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@href='job/test_1/']")))

    #label=browser.find_element(By.XPATH, "//*[@href='job/test_1/']")
    assert label.text == "test_1"
