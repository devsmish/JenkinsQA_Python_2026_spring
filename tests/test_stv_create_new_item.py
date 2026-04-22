import time

from selenium.webdriver.common.by import By


def test_stv_create_new_item(browser):
    browser.find_element(By.XPATH, "//a[.//span[text()='New Item']]").click()
    time.sleep(1)

    assert "New Item" in browser.title

    browser.find_element(By.XPATH, "//input[@name='name']").send_keys("My_First_Test")

    browser.find_element(By.XPATH, '//div[@class="desc"]').click()

    browser.find_element(By.XPATH, '//button[@id="ok-button"]').click()
    time.sleep(1)
    assert "General" in browser.find_element(By.XPATH, '//h2[@id="general"]').text
    browser.find_element(By.XPATH, '//*[@id="main-panel"]/form/div[1]/div[2]/div/div[2]/textarea').send_keys("My_First_Test")
    time.sleep(1)
    browser.find_element(By.XPATH, "//label[text()='Do not allow the pipeline to resume if the controller restarts']").click()
    time.sleep(1)
    element = browser.find_element(By.XPATH, "//label[normalize-space()='GitHub hook trigger for GITScm polling']")
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()
    time.sleep(1)
    element_save = browser.find_element(By.XPATH, "//button[@name = 'Submit']")
    browser.execute_script("arguments[0].scrollIntoView(true);", element_save)
    element_save.click()
    assert "My_First_Test" in browser.title