import time
from selenium.webdriver.common.by import By


def test_treugolnik(browser):
    browser.get("https://playground.learnqa.ru/puzzle/triangle")
    assert 'LearnQA - Playground' in browser.title
    side_a = browser.find_element(By.CLASS_NAME,'js_a')
    side_a.clear()
    side_a.send_keys('5')
    side_b = browser.find_element(By.CLASS_NAME,'js_b')
    side_b.clear()
    side_b.send_keys('3')
    side_c = browser.find_element(By.CLASS_NAME,'js_c')
    side_c.clear()
    side_c.send_keys('4')
    button = browser.find_element(By.XPATH,'//*[@id="puzzle"]/div[2]/div[2]/div[6]/button[1]')
    button.click()
    # assert 'Это прямоугольный треугольник.' in browser.find_element(By.XPATH,'//*[@id="puzzle"]/div[2]/div[2]/div[2]/text()[1])')

