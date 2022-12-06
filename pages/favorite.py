from selenium.webdriver.common.by import By

class FavPage:
    def __init__(self, driver):
        self.driver=driver

    def fav_ads(self):
        return self.driver.find_elements(By.XPATH, "//div[@id='bulletinId']")
