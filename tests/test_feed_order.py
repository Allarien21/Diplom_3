import allure

import data
from pages.feed_order_page import FeedOrderPage


class TestOrderFeed:

    @allure.title('Получение информации о заказе')
    @allure.description('Переход на страницу заказов, выбор первого заказа. Просмотр описания')
    def test_order_info(self, driver):
        order_feed = FeedOrderPage(driver)
        element = order_feed.get_info_order()
        assert element.text == data.INFO_ORDER

    @allure.title('Проверка отображения заказа пользователя на странице "Лента заказов"')
    @allure.description('Логинимся, оформляем заказ, сравниваем номер заказа с этим номером в Ленте заказов')
    def test_order_from_history(self, driver,user_credentials):
        order_feed = FeedOrderPage(driver)
        order_feed.click_personal_acc()
        order_feed.login_user(user_credentials['email'], user_credentials['password'])
        order_feed.add_ingredient_to_order()
        assert order_feed.get_new_order_number() in order_feed.get_orders_list()

    @allure.title('Проверка увеличения счетчика заказов, выполненных за все время"')
    @allure.description('Логинимся, оформляем заказ, проверяем что общий счетчик заказов увеличился на 1')
    def test_counter_all_time(self, driver,user_credentials):
        order_feed = FeedOrderPage(driver)
        data_1 = order_feed.get_orders_all()
        order_feed.click_personal_acc()
        order_feed.login_user(user_credentials['email'], user_credentials['password'])
        order_feed.add_ingredient_to_order()
        data_2 = order_feed.get_new_order_number()
        assert int(data_2) == int(data_1) + 1

    @allure.title('Проверка увеличения счетчика заказов, выполненных за все время"')
    @allure.description('Логинимся, оформляем заказ, проверяем что дневной счетчик заказов увеличился на 1')
    def test_counter_today(self, driver, user_credentials):
        order_feed = FeedOrderPage(driver)
        order_feed.click_personal_acc()
        order_feed.login_user(user_credentials['email'], user_credentials['password'])
        data_1 = order_feed.get_orders_today()
        order_feed.get_order_today_info()
        data_2 = order_feed.get_orders_today()
        assert int(data_2) == int(data_1) + 1

    @allure.title('Проверка увеличения счетчика заказов, выполненных за все время"')
    @allure.description('Логинимся, оформляем заказ, проверяем что дневной счетчик заказов увеличился на 1')
    def test_counter_today(self, driver, user_credentials):
        order_feed = FeedOrderPage(driver)
        order_feed.click_personal_acc()
        order_feed.login_user(user_credentials['email'], user_credentials['password'])
        order_feed.add_ingredient_to_order()
        data_1 = order_feed.get_new_order_number()
        data_2 = order_feed.get_new_order_in_work()
        assert  data_1 in data_2

