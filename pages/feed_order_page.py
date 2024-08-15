import allure

from Locators.main_locator import Main
from Locators.order_locator import Order
from pages.base_page import BasePage
from Locators.login_locator import Login
class FeedOrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по Личному кабинету')
    def click_personal_acc(self):
        self.find_element_located(Login.PERSONAL_ACC).click()

    @allure.step('Клик по елементу "Лента заказов", и просмотр детали заказа')
    def get_info_order(self):
        self.find_element_clickable(Order.ORDER_FEED)
        self.find_element_clickable(Order.ORDER_LI)
        return self.find_element_located(Order.ORDER_INFO)

    @allure.step('Добавить интгридиенты в заказ')
    def add_ingredient_to_order(self):
        source_element = self.wait_and_find_element(Main.INGREDIENT)
        target_element = self.wait_and_find_element(Main.ORDER_BASKET)
        self.drag_and_drop(source_element, target_element)
        self.find_element_clickable(Order.GREATE_ORDER)

    @allure.step('Ввести почту и пароль')
    def login_user(self, email, password):
        self.find_element_located(Login.EMAIL).send_keys(email)
        self.find_element_located(Login.PASSWORD).send_keys(password)
        self.find_element_located(Login.LOGIN_BUTTON).click()

    @allure.step('Получение номера оформленного заказа')
    def get_new_order_number(self):
        self.wait_invisible(Order.GET_PRICE_ORDER, '9999')
        return self.get_text_by_element(Order.GET_PRICE_ORDER)

    @allure.step('Получение номера готового заказа')
    def get_orders_list(self):
        self.find_element_clickable(Order.CLOSE_BUTTON)
        self.find_element_clickable(Order.ORDER_FEED)
        return self.get_text_by_element(Order.ORDERS_NUMBERS)

    @allure.step('Получение общее кол-во заказов за все время')
    def get_orders_all(self):
        self.find_element_clickable(Order.ORDER_FEED)
        self.wait_and_find_element(Order.ORDER_ALL_TIME)
        return self.get_text_by_element(Order.ORDER_ALL_TIME)

    @allure.step('Получение общее кол-во заказов за сегодня')
    def get_orders_today(self):
        self.find_element_clickable(Order.ORDER_FEED)
        self.wait_and_find_element(Order.ORDER_TODAY)
        return self.get_text_by_element(Order.ORDER_TODAY)

    @allure.step('Оформлени заказа и проверка кол-ва заказов')
    def get_order_today_info(self):
        self.find_element_clickable(Main.CONSTRUCTOR)
        source_element = self.wait_and_find_element(Main.INGREDIENT)
        target_element = self.wait_and_find_element(Main.ORDER_BASKET)
        self.drag_and_drop(source_element, target_element)
        self.find_element_clickable(Order.GREATE_ORDER)
        self.wait_invisible(Order.GET_PRICE_ORDER, '9999')
        self.find_element_clickable(Order.CLOSE_BUTTON)
        self.find_element_clickable(Order.ORDER_FEED)


    def get_new_order_in_work(self):
        self.find_element_clickable(Order.CLOSE_BUTTON)
        self.find_element_clickable(Order.ORDER_FEED)
        self.wait_and_find_element(Order.IN_PROGRESS)
        return self.get_text_by_element(Order.ORDERS_NUMBERS)

