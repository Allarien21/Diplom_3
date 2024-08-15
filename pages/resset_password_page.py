import allure
import urls

from constants import Constants
from Locators.login_locator import Login
from pages.base_page import BasePage


class RessetPassword(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    @allure.step('Открытие страницы восстановления пароля')
    def click_resset_password(self):
        self.find_element_located(Login.PERSONAL_ACC).click()
        self.presence_element_located(Login.RESTORE_PASSWORD).click()

    @allure.step('Ввод данных и ожидание перехода на новую страницу')
    def data_input_click_resset(self):
        self.find_element_located(Login.EMAIL).send_keys(Constants.EMAIL)
        self.find_element_located(Login.RESET_BUTTON).click()
        self.wait_for_url_to_be(urls.URL_RESSET)

    @allure.step('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def click_show_button(self):
        self.presence_element_located(Login.SHOW_BUTTON).click()
        return self.find_element_located(Login.ACTIVE_FIELD)


