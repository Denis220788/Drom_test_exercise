from selenium.webdriver.common.by import By


class AuthPage():
    def __init__(self, driver):
        self.driver=driver

    def phone_mail_login(self):
        return self.driver.find_element(By.ID, "sign")

    def password(self):
        return self.driver.find_element(By.ID, "password")

    def enter_btn(self):
        return self.driver.find_element(By.ID, "signbutton")