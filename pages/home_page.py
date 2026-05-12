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


    def get_project_names_list(self):
        project_elements = self.driver.find_elements(By.CLASS_NAME, "jenkins-table__link")
        project_names = [element.text for element in project_elements]

        return project_names

      
    def show_dropdown_menu_from_profile_icon(self):
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(By.ID, "root-action-UserAction")
        ).perform()

        return self

      
    def dropdown_menu_sign_out_click(self):
        self.wait10.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[@class="jenkins-dropdown"]//a[@href="/logout"]')
            )
        ).click()

        return LoginPage(self.driver)
