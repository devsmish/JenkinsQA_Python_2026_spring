from selenium.webdriver.common.by import By

def test_new_item_page_opens_after_click(browser):
    element = browser.find_element(By.XPATH, '//a[contains(., "New Item")]')
    element.click()
    header = browser.find_element(By.XPATH, '//h1[contains(., "New Item")]')
    assert "http://localhost:8080/view/all/newJob" in browser.current_url
    assert "New Item" in browser.title
    assert header.text == "New Item"