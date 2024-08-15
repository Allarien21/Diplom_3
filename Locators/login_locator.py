from selenium.webdriver.common.by import By
class Login:
    PERSONAL_ACC= (By.XPATH, "//a[@href='/account']")  # Кнопка Личного кабинета

    EMAIL = (By.XPATH, "//input[@type='text']")  # Поле ввода почты для авторизации
    PASSWORD = (By.XPATH, "//input[contains(@type, 'password')]")  # Поле ввода пароля
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button')]")  # Кнопка Войти

    RESTORE_PASSWORD = (By.XPATH, "//a[@href= '/forgot-password']") # Кнопка восстановление пароля
    RESET_BUTTON = (By.XPATH, "//button[contains(@Class, 'button_button')]") # Кнопка Восстановить
    SHOW_BUTTON = (By.XPATH,"//div[contains(@class,'input__icon-action')]") # Кнопка показать пароль
    ACTIVE_FIELD = (By.XPATH,"//div[@class ='input__container']/div[contains( @class,'input_status_active')]")#

    ORDER_HISTORY_BTN = (By.XPATH, "//a[@href='/account/order-history']")  # Кнопка Истории заказов в личном кабинете
    ORDER_HISTORY = (By.XPATH,"//li[contains(@class, 'OrderHistory_listItem')]") #Список первого заказа
    OUT_LC_BTN = (By.XPATH, "(//button[contains(@class,'Account_button')])")# Кнопка выхода из личного кабинета

