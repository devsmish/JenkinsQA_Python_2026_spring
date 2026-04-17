from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def test_python_search(browser):
    """Тест результатов поиска сайта python"""
    browser.get("https://www.python.org/")

    search_field = browser.find_element(By.NAME, "q")
    search_field.clear()
    search_field.send_keys("selenium")
    search_field.send_keys(Keys.ENTER)

    link = browser.find_element(By.LINK_TEXT, "Job - Python Developer")
    href = link.get_attribute("href")

    assert href == "https://www.python.org/jobs/8060/"