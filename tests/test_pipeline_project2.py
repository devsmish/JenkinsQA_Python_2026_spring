
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.dependency()
def test_pipeline_project2(browser):
    test="test_1"
    wait = WebDriverWait(browser, 5)

    browser.find_element(By.LINK_TEXT, "New Item").click()
    browser.find_element(By.ID, "name").send_keys(test)

    browser.find_element(By.XPATH,"//ul/li//span[text()='Pipeline']").click()
    browser.find_element(By.ID, "ok-button").click()


    wait.until(EC.element_to_be_clickable((By.NAME,"Submit"))).click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='app-jenkins-logo']"))).click()

    wait = WebDriverWait(browser, 10)
    label=wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@href='job/test_1/']"))).text


    assert label == test

@pytest.mark.dependency(depends=["test_pipeline_project2"])
def test_add_discription_Pipeline(browser):
    text_Description = "Description here"

    browser.find_element (By.LINK_TEXT, "test_1").click()

    wait = WebDriverWait(browser, 5)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Configure']"))).click()
    WebDriverWait(browser, 5)

    browser.find_element(By.NAME, "description").send_keys(text_Description)
    WebDriverWait(browser, 10)

    browser.find_element(By.NAME, "Submit").click()
    WebDriverWait(browser, 10)


    assert browser.find_element (By.ID, "description-content").text==text_Description
