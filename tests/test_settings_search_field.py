from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from conftest import browser


def _get_field_search(driver):
    return driver.find_element(By.ID, 'settings-search-bar')


def _get_manage_jenkins_btn(driver):
    return driver.find_element(By.ID, 'root-action-ManageJenkinsAction')


def test_checking_the_dropdown_when_entering_one_letter(browser):
    _get_manage_jenkins_btn(browser).click()

    _get_field_search(browser).send_keys('t')
    items = browser.find_elements(
        By.XPATH,
        '//*[contains(@class, "jenkins-search__results-container--visible")]//a[contains(translate(., "T", "t"), "t")]'
    )

    assert len(items) > 1


def test_checking_the_dropdown_when_entering_full_name_settings(browser):
    _get_manage_jenkins_btn(browser).click()

    _get_field_search(browser).send_keys('Security')
    item = browser.find_element(
        By.XPATH,
        '//*[contains(@class,"jenkins-search__results-container--visible")]//a[normalize-space()="Security"]'
    )

    assert item.text.strip() == 'Security'


def test_clear_search_field_via_keyboard_and_button(browser):
    _get_manage_jenkins_btn(browser).click()
    field = _get_field_search(browser)

    field.send_keys('System')
    field.send_keys(Keys.CONTROL + 'a')
    field.send_keys(Keys.BACK_SPACE)

    field.send_keys('Manage Jenkins')
    field.clear()

    assert field.get_attribute('value') == ''
    assert 'No results' in browser.find_element(By.CSS_SELECTOR, '.jenkins-search__results-container').text