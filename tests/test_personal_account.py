import allure

import urls
from pages.personal_account_page import PersonalAccPage


class TestPersonalAcc:

    @allure.title('Переход по клина на Личный кабинет')
    @allure.description('Регистрируем пользователя, кликаем на Личный кабинет. Проверяем урл')
    def test_user_login(self, driver, user_credentials):
        user_page = PersonalAccPage(driver)
        user_page.click_personal_acc()
        user_page.login_user(user_credentials['email'], user_credentials['password'])
        user_page.click_personal_acc()
        assert user_page.get_current_url() == urls.URL_PROFILE

    @allure.title('Переход в раздел «История заказов»')
    @allure.description('Регистрируем пользователя, кликаем на Личный кабинет. Проверяем урл')
    def test_order_history(self, driver, user_credentials):
        user_page = PersonalAccPage(driver)
        user_page.click_personal_acc()
        user_page.login_user(user_credentials['email'], user_credentials['password'])
        user_page.click_personal_acc()
        user_page.click_history_order()
        assert user_page.get_current_url() == urls.URL_HISTORY

    @allure.title('Создание заказа зарегистрированным пользователем')
    @allure.description('Регистрируем пользователя, делаем заказ, проверяем поп-ап')
    def test_out_user_account(self, driver, user_credentials):
        user_page = PersonalAccPage(driver)
        user_page.click_personal_acc()
        user_page.login_user(user_credentials['email'], user_credentials['password'])
        user_page.click_personal_acc()
        user_page.click_out_account()
        assert user_page.get_current_url() == urls.URL_LOGIN