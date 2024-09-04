import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from Handicap.Pages.login_page import LoginPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    # Yield the WebDriver instance
    yield driver
    # Close the WebDriver instance
    driver.close()


def test_login(driver):
    #login
    login_page = LoginPage(driver)
    login_page.login_credential('https://test.jobs.hi-bd.org/admin/login',
                                'admin',
                                '123456')

    time.sleep(3)
    login_page.click_login()
    time.sleep(3)
