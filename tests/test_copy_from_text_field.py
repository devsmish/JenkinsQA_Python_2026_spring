from time import sleep
from selenium.webdriver.common.by import By


def test_copy_from_text_field(browser):
    """TC_01.003.01. Verifies 'Copy from' Text Field available"""
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    browser.find_element(By.XPATH, "//input[@id='name']").send_keys("my_first_pipeline")
    browser.find_element(By.XPATH, "(//li[@class='org_jenkinsci_plugins_workflow_job_WorkflowJob'])[1]").click()
    browser.find_element(By.XPATH, "//button[@id='ok-button']").click()
    browser.find_element(By.XPATH, "(//textarea[@name='description'])[1]").send_keys("My first pipeline")
    browser.maximize_window()
    browser.execute_script("window.scrollBy({ top: 1200, left: 0, behavior: 'auto' });")
    sleep(1)
    browser.find_element(By.XPATH, "(//button[normalize-space()='Save'])[1]").click()
    browser.find_element(By.XPATH, "(//a[@class='app-jenkins-logo'])[1]").click()
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    browser.execute_script("window.scrollBy({ top: 800, left: 0, behavior: 'auto' });")
    sleep(1)
    text_field = browser.find_element(By.XPATH, "(//label[normalize-space()='Copy from'])[1]")
    browser.find_element(By.XPATH, "(//input[@id='from'])[1]").click()
    browser.find_element(By.XPATH, "(//input[@id='from'])[1]").send_keys("my_first_pipeline")

    assert text_field.text == "Copy from"

#This is just a comment to introduce a change to allow new commit and push.
