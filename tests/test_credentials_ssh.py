from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
test_id = "testID"

def test_add_credentials_ssh_username(browser):

    browser.find_element(By.ID, 'root-action-ManageJenkinsAction').click()
    browser.find_element(By.CSS_SELECTOR, "a[href='credentials']").click()

    browser.find_element(By.CSS_SELECTOR, "button[data-type='credentials-add-store-item']").click()
    browser.find_element(By.XPATH, "//div[contains(text(),'SSH Username with private key')]").click()
    browser.find_element(By.ID, 'cr-dialog-next').click()

    Select(browser.find_element(By.NAME,'_.scope')).select_by_value('SYSTEM')
    browser.find_element(By.NAME,'_.id').send_keys(test_id)
    browser.find_element(By.NAME,'_.description').send_keys("testDescription")
    browser.find_element(By.NAME,'_.username').send_keys("testUsername")
    browser.find_element(By.XPATH, "//label[normalize-space()='Treat username as secret']").click()
    browser.find_element(By.XPATH, "//label[normalize-space()='Enter directly']").click()
    browser.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
    browser.find_element(By.NAME, '_.privateKey').send_keys("testKey")
    browser.find_element(By.NAME, '_.passphrase').send_keys("testPassphrase")
    browser.find_element(By.ID, 'cr-dialog-submit').click()

    assert browser.find_element(By.XPATH, "//a[normalize-space()='testID']").text == test_id