import urls
import allure

from Locators.main_locator import Main
from pages.base_page import BasePage
from Locators.login_locator import Login
class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажать на кномпку личного кабинета')
    def click_my_account(self):
        self.find_element_located(Main.PERSONAL_ACC).click()

    @allure.step('Переход на страницу Контсруктор')
    def transition_for_main_constructor(self):
        self.find_element_located(Main.PERSONAL_ACC).click()
        self.wait_for_url_to_be(urls.URL_LOGIN)
        self.find_element_located(Main.CONSTRUCTOR).click()
        return self.find_element_located(Main.ASSEMBLE_BURGER)

    @allure.step('Переход на страницу Лента заказов')
    def transition_for_main_order(self):
        self.find_element_located(Main.ORDER_FEED).click()
        self.wait_for_url_to_be(urls.URL_FEED)
        return self.find_element_located(Main.FEED_ORDER_TEXT)

    @allure.step('Открытие Деталей заказа')
    def ingredient_detail(self):
        self.find_element_located(Main.INGREDIENT).click()
        return self.find_element_located(Main.INGREDIENT_DETAIL)

    @allure.step('Закрытие окна Деталей заказа')
    def close_ingredient_detail(self):
        self.find_element_located(Main.INGREDIENT).click()
        self.find_element_located(Main.CLOSE).click()

    @allure.step('Получение атрибута для проверки закрытия окна с инфо об ингредиенте')
    def ingredient_info_closed(self):
        return self.get_attribute(Main.WINDOW_INFO_INGREDIENT, 'class')

    @allure.step('Добавить интгридиенты в заказ')
    def add_ingredient_to_order(self):
        source_element = self.wait_and_find_element(Main.INGREDIENT)
        target_element = self.wait_and_find_element(Main.ORDER_BASKET)
        self.drag_and_drop(source_element, target_element)
        return self.find_element_located(Main.COUNTER)

    @allure.step('Ввести почту и пароль')
    def login_user(self, email, password):
        self.find_element_located(Login.EMAIL).send_keys(email)
        self.find_element_located(Login.PASSWORD).send_keys(password)
        self.find_element_located(Login.LOGIN_BUTTON).click()

    @allure.step('Нажать оформление заказа, получить  поп ап')
    def place_an_order(self):
        self.find_element_located(Main.PLACE_ORDER).click()
        return self.presence_element_located(Main.GRATE_ORDER)
