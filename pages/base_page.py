from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait10 = WebDriverWait(driver, timeout)
        self.wait5 = WebDriverWait(driver, 5)

    def go_home_page(self):
        from pages.home_page import HomePage
        self.driver.find_element(By.XPATH, "//span[@class='jenkins-mobile-hide']").click()

        return HomePage(self.driver)