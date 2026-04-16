import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    """Открытие и закрытие браузера перед и после каждого теста"""
    driver = webdriver.Chrome()
    yield driver
    driver.close()


def test_wikipedia_search(browser):
    """
    Search box test on the Wikipedia main page
    """

    test_url = "https://wikipedia.org"
    search_query = "Пушкин"
    input_search_locator = (By.XPATH, '//input[@id="searchInput"]')
    heading_locator = (By.XPATH, '//*[@id="firstHeading"]')

    # Открываем главную страницу Википедии
    browser.get(test_url)

    # Ищем поле ввода поискового запроса
    input_box = browser.find_element(*input_search_locator)

    # Передаем в поле наш запрос search_query и нажимаем Enter
    input_box.send_keys(search_query + Keys.ENTER)

    # Ждем когда изменится URL страницы
    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_changes(test_url))

    # Ищем заголовок статьи на новой странице и считываем содержимое заголовка в переменную
    heading = wait.until(EC.presence_of_element_located(heading_locator)).text

    # Проверяем, что заголовок статьи содержит наш поисковый запрос
    assert search_query in heading
