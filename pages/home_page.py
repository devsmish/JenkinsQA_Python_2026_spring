from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage
from pages.new_item_page import NewItemPage
from pages.login_page import LoginPage


class HomePage(BasePage):
    def new_item_click(self):
        self.wait10.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/view/all/newJob']"))
        ).click()

        return NewItemPage(self.driver)

    def show_dropdown_menu_from_profile_icon(self):
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(By.ID, "root-action-UserAction")
        ).perform()

        return self

    def dropdown_menu_item_click(self, name):
        items = {
            "Theme": {},
            "My views": {},
            "Account": {},
            "Appearance": {},
            "Preferences": {},
            "Security": {},
            "Experiments": {},
            "Credentials": {},
            "Sign out": {
                "xpath": '//div[@class="jenkins-dropdown"]//a[@href="/logout"]',
                "result page": LoginPage,
            },
        }

        self.wait10.until(
            EC.element_to_be_clickable((By.XPATH, items[name]["xpath"]))
        ).click()
        current_page = items[name]["result page"]

        return current_page(self.driver)
