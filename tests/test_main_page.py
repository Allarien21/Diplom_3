import allure
import data

from pages.main_page import MainPage

class TestMainPage:
    @allure.title('Проверка перехода в "Конструктор"')
    @allure.description('Кликаем на кнопку "Личного кабинета", кликаем по кнопке "Конструктор", проверяем что на странице есть блок "Соберите бургер"')
    def test_transition_for_page(self,driver):
        page = MainPage(driver)
        element = page.transition_for_main_constructor()
        assert element.text == data.constructor

    @allure.title('Проверка перехода на "Ленту заказов"')
    @allure.description('Кликаем на кнопку "Лента заказов",проверяем что на странице есть блок "Лента заказов"')
    def test_transition_for_order(self, driver):
        page = MainPage(driver)
        element = page.transition_for_main_order()
        assert element.text == data.feed_order

    @allure.title('Проверка перехода на "Окно с деталями ингридиента"')
    @allure.description('Кликаем на кнопку "Лента заказов",кликаем по первому заказу, проверяем что на странице есть блок "Состав"')
    def test_check_popup_order(self, driver):
        page = MainPage(driver)
        element = page.ingredient_detail()
        assert element.text == data.ingredient_detail

    @allure.title('Проверка закрытия высплывающего окна с деталями ингридиента"')
    @allure.description('Кликаем на ингредиент, нажимаем крестик на всплывающем окне,проверяем что всплывающее окно закрылось')
    def test_info_closed_ingredient(self,driver):
        page = MainPage(driver)
        page.close_ingredient_detail()
        assert 'opened' not in page.ingredient_info_closed()

    @allure.title('Проверка увеличенеи счетчика товара при добавлению в "корзину"')
    @allure.description('Кликаем на ингредиент, перетаскиваем в "корзину"проверяем счетчик')
    def test_add_ingredient(self, driver):
        page = MainPage(driver)
        element = page.add_ingredient_to_order()
        assert element.text == str(2)

    @allure.title('Создание заказа зарегистрированным пользователем')
    @allure.description('Регистрируем пользователя, делаем заказ, проверяем поп-ап')
    def test_create_order_at_user_login(self, driver,user_credentials):
       page = MainPage(driver)
       page.click_my_account()
       page.login_user(user_credentials['email'],user_credentials['password'])
       page.add_ingredient_to_order()
       element = page.place_an_order()
       assert element.text == data.grate_order