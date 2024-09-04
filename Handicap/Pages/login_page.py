import time

from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.txt_loginUserName = (By.NAME, "username")
        self.txt_loginPassword = (By.NAME, "password")
        self.btn_login = (By.XPATH, "//button[@type='submit']")

    def login_credential(self, url, username, password):
        self.driver.get(url)
        time.sleep(3)
        self.driver.find_element(*self.txt_loginUserName).send_keys(username)
        time.sleep(3)
        self.driver.find_element(*self.txt_loginPassword).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.btn_login).click()
