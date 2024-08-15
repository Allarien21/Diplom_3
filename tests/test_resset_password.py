import allure
import urls

from pages.resset_password_page import RessetPassword


class TestResset:
    @allure.title('Проверка перехода на страницу восстановления пароля')
    @allure.description('Кликаем на кнопку "Личный кабинет", кликаем на кнопку "Восстановить пароль", \
                            проверка переход на страницу восстановления пароля')
    def test_transition_to_password_recovery_page(self, driver):
        page = RessetPassword(driver)
        page.click_resset_password()
        assert page.get_current_url() == urls.URL_FORGOT

    @allure.title('Проверка ввода email и клика по кнопке "Восстановить"')
    @allure.description('Переходим на страницу восстановления пароля, вводим email, кликаем на кнопку "Восстановить"\
                        проверяем урл')
    def test_redirect_to_password_recovery_page(self, driver):
        page = RessetPassword(driver)
        page.click_resset_password()
        page.data_input_click_resset()
        assert page.get_current_url() == urls.URL_RESSET

    @allure.title('Проверка активности поля Пароль по клику на показать/скрыть')
    @allure.description('Переходим на страницу восстановления пароля, заполняем поле email, кликаем на кнопку \
                                  "Восстановить", кликаем на значок глаза, проверяем, что поле стало активным')
    def test_show_field_is_active(self, driver):
        page = RessetPassword(driver)
        page.click_resset_password()
        page.data_input_click_resset()
        active_field = page.click_show_button()
        assert active_field.is_displayed()