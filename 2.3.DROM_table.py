import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url="http://auto.drom.ru/"
driver_service = Service(executable_path="D:/Project/Drom/chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()
driver.implicitly_wait(2)
driver.get(url)
#time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(),'Другой город')]").click()
#time.sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder='поиск города, региона']").send_keys("Приморский край")
driver.find_element(By.XPATH, "//input[@placeholder='поиск города, региона']").send_keys(Keys.ENTER)
show_all = driver.find_element(By.XPATH, "//div[contains(text(),'Показать все')]")
ActionChains(driver).scroll_to_element(show_all)
show_all.click()
list_of_list = driver.find_elements(By.XPATH, "//div[@class='css-ofm6mg exkrjba0']")
spisok = []
spisok_1 = []

for i in range(len(list_of_list)):
    spisok.append(list_of_list[i].text.split("\n"))
spisok_1 = [item for sublist in spisok for item in sublist]
spisok_1.sort()
result_spisok = []

for j in range(len(spisok_1)):
    result_spisok.append(spisok_1[j].split(" "))
print(result_spisok)








