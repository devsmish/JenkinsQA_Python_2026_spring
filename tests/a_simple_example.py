    # Test # 2
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# driver = webdriver.Chrome()
#
# driver.get("https://www.selenium.dev/selenium/web/web-form.html")
#
# driver.implicitly_wait(0.5)
#
# text_box = driver.find_element(by=By.NAME, value="my-textarea")
# text_box.send_keys("My city")
# time.sleep(1)
#
#
# #         Dropdowns
# dropdown_select = driver.find_element(By.NAME, "my-select")
# select = Select(dropdown_select)
#
# select.select_by_visible_text("Two")
#
# assert select.first_selected_option.text == "Two"
# time.sleep(1)
#
# dropdown_datalist = driver.find_element(by=By.NAME, value="my-datalist")
# dropdown_datalist.send_keys("San Francisco")
# time.sleep(1)
#
# #       Checkboxes etc
# checked_checkbox = driver.find_element(By.ID, "my-check-1")
# checked_checkbox.click()
# time.sleep(3)
#
# Checked_radio = driver.find_element(By.ID, "my-radio-1")
# Checked_radio.click()
#
# assert Checked_radio.is_selected()
#
# time.sleep(1)
#
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
# submit_button.click()
#
# time.sleep(2)
#
# driver.quit()




#               Test WIKIPEDIA

driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

driver.implicitly_wait(0.5)

search_box = driver.find_element(By.ID, "searchInput")

search_box.send_keys("Selenium")

time.sleep(2)

search_button = driver.find_element(By.CSS_SELECTOR, "button.cdx-search-input__end-button")
search_button.click()

time.sleep(2)

driver.quit()



# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
#
# driver.get("https://www.selenium.dev/selenium/web/web-form.html")
#
# driver.implicitly_wait(0.5)

# title = driver.title
# assert driver.title == "Web form"

#
# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
#
# text_box.send_keys("Selenium")
#
# time.sleep(2)
#
# submit_button.click()
#
# message = driver.find_element(by=By.ID, value="message")
# text = message.text
#
# time.sleep(2)
#
# print(text)
#
# driver.quit()

