from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



def test_quick_change_theme_not_able(browser):
    ActionChains(browser).move_to_element(browser.find_element(By.ID, 'root-action-UserAction')).perform()
    browser.find_element(By.CSS_SELECTOR, 'a.jenkins-dropdown__item[href $= "appearance"]').click()

    ActionChains(browser).move_to_element(browser.find_element(By.ID, 'root-action-UserAction')).perform()
    assert not browser.find_elements(By.ID, 'account-theme-picker'), "Error: Quick theme change block is displayed, when the Appearance page is open"