
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest

pipeline_name = "Pipeline_Name"

@pytest.mark.skip()
def test_create_pipeline_project(browser):
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    browser.find_element(By.ID, "name").send_keys(pipeline_name)
    browser.find_element(By.CLASS_NAME, "org_jenkinsci_plugins_workflow_job_WorkflowJob").click()

    browser.find_element(By.ID, "ok-button").click()

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()

    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.jenkins-mobile-hide"))).click()

    created_pipeline = browser.find_element(By.XPATH, "(//a[@href='job/Pipeline_Name/'])[1]").text

    assert created_pipeline == pipeline_name
