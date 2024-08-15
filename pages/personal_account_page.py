import urls
import allure


from pages.base_page import BasePage
from Locators.login_locator import Login
class PersonalAccPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по Личному кабинету')
    def click_personal_acc(self):
        self.find_element_located(Login.PERSONAL_ACC).click()

    @allure.step('Нажатие выхода из личного кабинета')
    def click_out_account(self):
        self.find_element_located(Login.OUT_LC_BTN).click()
        self.wait_for_url_to_be(urls.URL_LOGIN)

    @allure.step('Нажатие Истории закозав из личного кабинета')
    def click_history_order(self):
        self.find_element_located(Login.ORDER_HISTORY_BTN).click()
        self.wait_for_url_to_be(urls.URL_HISTORY)

    @allure.step('Ввести почту и пароль')
    def login_user(self, email, password):
        self.find_element_located(Login.EMAIL).send_keys(email)
        self.find_element_located(Login.PASSWORD).send_keys(password)
        self.find_element_located(Login.LOGIN_BUTTON).click()