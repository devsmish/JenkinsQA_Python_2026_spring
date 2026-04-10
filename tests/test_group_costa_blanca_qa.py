from selenium.webdriver.common.by import By


def test_storyia_submit_form(browser):
    browser.get("https://www.selenium.dev/selenium/web/web-form.html")

    text_box = browser.find_element(By.NAME, "my-text")
    submit_button = browser.find_element(By.CSS_SELECTOR, "button")

    text_box.send_keys("Storyia")
    submit_button.click()

    message = browser.find_element(By.ID, "message").text

    assert message == "Received!"

def test_storyia_checkbox_selected(browser):
    browser.get("https://www.selenium.dev/selenium/web/web-form.html")

    checkbox = browser.find_element(By.ID, "my-check-2")
    checkbox.click()

    assert checkbox.is_selected()
