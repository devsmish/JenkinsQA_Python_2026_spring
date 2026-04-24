from selenium.webdriver.common.by import By

def test_open_new_item_page(browser):
    browser.get("http://localhost:8080")

    browser.find_element("link text", "New Item").click()

    assert "/newJob" in browser.current_url