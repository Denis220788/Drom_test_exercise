import time


from selenium.webdriver import ActionChains

from pages.sell_car import SellCarPage
from pages.enter_and_reg import AuthPage
from pages.favorite import FavPage

# №2.1. Тест на отсутствие проданных машин на первой странице поиска
def test_no_sold_car_on_page_one(driver_filter):
    sell_page = SellCarPage(driver_filter)
    sold_car = sell_page.sold_car()
    assert len(sold_car) == 0

# №2.1. Тест на отсутствие проданных машин на второй странице поиска
def test_no_sold_car_on_page_two(driver_filter):
    sell_page = SellCarPage(driver_filter)
    actions = ActionChains(driver_filter)
    scnd_page = sell_page.second_page()
    actions.scroll_to_element(scnd_page)
    scnd_page.click()
    not_sold_car = sell_page.not_sold_car()
    sold_car = sell_page.sold_car()
    assert len(sold_car) == 0

# №2.1. Тест на наличие пробега в объявлениях на первой странице поиска
def test_all_ads_has_mileage_on_page_one(driver_filter):
    sell_page = SellCarPage(driver_filter)
    ads = sell_page.amount_car()
    ads_with_mileage = sell_page.ads_with_mileage()
    assert len(ads) == len(ads_with_mileage)

# №2.1. Тест на наличие пробега в объявлениях на второй странице поиска
def test_all_ads_has_mileage_on_page_two(driver_filter):
    sell_page = SellCarPage(driver_filter)
    actions = ActionChains(driver_filter)
    scnd_page = sell_page.second_page()
    actions.scroll_to_element(scnd_page)
    scnd_page.click()
    ads = sell_page.amount_car()
    ads_with_mileage = sell_page.ads_with_mileage()
    assert len(ads) == len(ads_with_mileage)

# №2.1. Тест на автомобили не старше 2007 года выпуска на первой странице поиска
def test_all_year_from_2007_on_page_one(driver_filter):
    sell_page = SellCarPage(driver_filter)
    ads_name = sell_page.ads_name()
    list_of_year = []
    for i in range(len(ads_name)):
        parts = ads_name[i].text.split(",")
        list_of_year.append(parts[1])
    print(list_of_year)
    for i in range(len(list_of_year)):
        assert int(list_of_year[i]) >= 2007

# №2.1. Тест на автомобили не старше 2007 года выпуска на второй странице поиска
def test_all_year_from_2007_on_page_two(driver_filter):
    sell_page = SellCarPage(driver_filter)
    actions = ActionChains(driver_filter)
    scnd_page = sell_page.second_page()
    actions.scroll_to_element(scnd_page)
    scnd_page.click()
    ads_name = sell_page.ads_name()
    list_of_year = []
    for i in range(len(ads_name)):
        parts = ads_name[i].text.split(",")
        list_of_year.append(parts[1])
    for i in range(len(list_of_year)):
        assert int(list_of_year[i]) >= 2007

# №2.2. Тест на авторизацию пользователя и добавление объявления о продаже в избранное
def test_auth_and_add_ads_to_fav(driver):
    sell_page = SellCarPage(driver)
    auth_page = AuthPage(driver)
    fav_page = FavPage(driver)
    actions = ActionChains(driver)
    sell_page.enter_reg().click()
    auth_page.phone_mail_login().send_keys("79134730244")
    auth_page.password().send_keys("DenisShilnikov")
    auth_page.enter_btn().click()
    time.sleep(2)
    sell_page.visit()
    sell_page.fav_btn().click()
    fav_ads_before = fav_page.fav_ads()
    amount_before = len(fav_ads_before)
    add_to_fav = sell_page.add_to_fav_btn()
    actions.scroll_to_element(add_to_fav)
    add_to_fav.click()
    sell_page.fav_btn().click()
    fav_ads_after = fav_page.fav_ads()
    amount_after = len(fav_ads_after)
    assert amount_after > amount_before

