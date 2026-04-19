import time
from selenium.webdriver.common.by import By

def test_create_new_folder(browser):
    '''Находим кнопку - New item, по которой кликаем'''
    new_item = browser.find_element(By.CSS_SELECTOR, "a[href='/view/all/newJob']")
    new_item.click()
    time.sleep(2)

    '''В поле для имени, вводим название папки'''
    input_name = browser.find_element(By.XPATH, '//*[@id="name"]')
    input_name.send_keys('My first folder')
    time.sleep(2)

    '''Кликнуть на карточку - Folder, чтобы выделить'''
    card_folder = browser.find_element(By.CLASS_NAME, 'com_cloudbees_hudson_plugins_folder_Folder')
    card_folder.click()
    time.sleep(2)

    '''Кликнуть кнопку - Ок'''
    button_ok = browser.find_element(By.ID, 'ok-button')
    button_ok.click()
    time.sleep(2)

    '''В поле вводим имя в поле Display name'''
    input_display_name = browser.find_element(By.NAME, '_.displayNameOrNull')
    input_display_name.send_keys('My folder')
    time.sleep(2)

    '''Вводим имя в поле Description'''
    input_description = browser.find_element(By.NAME, '_.description')
    input_description.send_keys('My description')
    time.sleep(2)

    '''Кликаем кнопку - Save'''
    button_save = browser.find_element(By.XPATH, '//button[@value="Save"]')
    button_save.click()
    time.sleep(2)

    '''Кликнуть на лого jenkins, чтобы вернуться на стартовую страницу'''
    logo = browser.find_element(By.ID, 'jenkins-head-icon')
    logo.click()
    time.sleep(2)
    browser.refresh()
    time.sleep(2)
