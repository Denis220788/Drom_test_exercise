from config import url
from selenium.webdriver.common.by import By


class SellCarPage():
    def __init__(self, driver):
        self.driver=driver

    def visit(self):
        self.driver.get(url)

    def marka(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Марка']")

    def model(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Модель']")

    def toplivo(self):
        return self.driver.find_element(By.XPATH, "//button[contains(text(),'Топливо')]")

    def gybrid(self):
        return self.driver.find_element(By.XPATH, "//div[contains(text(), 'Гибрид')]")

    def not_sell(self):
        return self.driver.find_element(By.XPATH, "//label[contains(text(),'Непроданные')]")

    def adv_search(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'Расширенный поиск')]")

    def mileage_from(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='от, км']")

    def year_from(self):
        return self.driver.find_element(By.XPATH, "//button[contains(text(),'Год от')]")

    def second_page(self):
        return self.driver.find_element(By.XPATH, "//a[@class='css-1jjais5 ena3a8q0' and contains(text(),'2')]")

    def enter_reg(self):
        return self.driver.find_element(By.XPATH, "//a[@data-ga-stats-name='auth_block_login']")

    def show(self):
        return self.driver.find_element(By.XPATH, "//div[contains(text(),'Показать')]")

    def sold_car(self):
        return self.driver.find_elements(By.XPATH, "//div[@class='css-r91w5p e3f4v4l2']")

    def not_sold_car(self):
        return self.driver.find_elements(By.XPATH, "//div[@class ='css-17lk78h e3f4v4l2']")

    def amount_car(self):
        return self.driver.find_elements(By.XPATH, "//a[@data-ftid='bulls-list_bull']")

    def ads_with_mileage(self):
        return self.driver.find_elements(By.XPATH, "//span[contains(text(),' тыс. км')]")

    def ads_name(self):
        return self.driver.find_elements(By.XPATH, "//div[@class='css-17lk78h e3f4v4l2']")

    def add_to_fav_btn(self):
        return self.driver.find_element(By.XPATH, "//div[@class='css-1rozdag']")

    def fav_btn(self):
        return self.driver.find_element(By.XPATH, "//div[@class='css-18895su e5173en1' and @xpath='1']")


