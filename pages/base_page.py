import allure

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск нужного элемента')
    def find_element_located(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator), message=f'Not found {locator}')

    @allure.step('Клик по нужному элементу')
    def find_element_clickable(self, locator, wait=None):
        if wait:
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(wait))
        self.wait_and_find_element(locator).click()

    @allure.step('Ожидание нужного элемента')
    def presence_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((locator)))

    @allure.step('Получение теуцщего урла')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ожадание получение урла')
    def wait_for_url_to_be(self,expected_url,time=30):
        try:
            WebDriverWait(self.driver, time).until(EC.url_to_be(expected_url))
        except TimeoutException:
            raise AssertionError(f"URL не изменился на {expected_url} в течение {time} секунд.")

    @allure.step('Поиск элемента')
    def wait_and_find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Получить значение атрибута элемента')
    def get_attribute(self, locator, value):
        return self.wait_and_find_element(locator).get_attribute(value)

    @allure.step('Перетащить элемент')
    def drag_and_drop(self, drag, drop):
        ActionChains(self.driver).drag_and_drop(drag, drop).pause(1).perform()

    @allure.step('Ожидание пока текст элемента не изменится')
    def wait_invisible(self, locator, value):
        self.wait_and_find_element(locator)
        return WebDriverWait(self.driver, 15).until_not(EC.text_to_be_present_in_element(locator, value))

    @allure.step('Получение текста элемента')
    def get_text_by_element(self, locator):
        return self.wait_and_find_element(locator).text