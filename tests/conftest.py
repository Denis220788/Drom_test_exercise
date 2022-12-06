import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service

from pages.sell_car import SellCarPage


@pytest.fixture(scope="function")
def driver_filter():
    driver_service = Service(executable_path="D:/Project/Drom/chromedriver.exe")
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    driver.implicitly_wait(5)
    sell_page = SellCarPage(driver)
    sell_page.visit()
    sell_page.marka().click()
    sell_page.marka().send_keys("Toyota")
    time.sleep(1)
    sell_page.marka().send_keys(Keys.ENTER)
    time.sleep(1)
    sell_page.model().click()
    sell_page.model().send_keys("Harrier")
    time.sleep(1)
    sell_page.model().send_keys(Keys.ENTER)
    sell_page.toplivo().click()
    sell_page.gybrid().click()
    sell_page.not_sell().click()
    sell_page.year_from().click()
    sell_page.year_from().send_keys("2007")
    sell_page.year_from().send_keys(Keys.ENTER)
    sell_page.adv_search().click()
    sell_page.mileage_from().send_keys("1")
    time.sleep(1)
    sell_page.show().click()
    time.sleep(2)
    yield driver

@pytest.fixture(scope="function")
def driver():
    driver_service = Service(executable_path="D:/Project/Drom/chromedriver.exe")
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    driver.implicitly_wait(5)
    sell_page = SellCarPage(driver)
    sell_page.visit()
    yield driver