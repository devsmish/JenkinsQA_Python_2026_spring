import os

import pytest
from selenium import webdriver

from common.jenkins_utils import login, logout, clear_data
from common.project_utils import ProjectUtils


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    for option in ProjectUtils.get_options():
        options.add_argument(option)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    clear_data()
    driver.get(ProjectUtils.get_url())
    login(driver)
    try:
        yield driver
    finally:
        try:
            logout(driver)
        finally:
            driver.quit()
