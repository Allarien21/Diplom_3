from selenium.webdriver.common.by import By

class Order:
    ORDER_FEED = (By.XPATH, "//a[@href='/feed']")  # Кнопка Лента заказов
    ORDER_LI = (By.XPATH,"//div[contains(@class, 'OrderHistory_dataBox')]") # Первый заказ
    ORDER_INFO = (By.XPATH, "//div[contains(@class,'Modal_orderBox')]/p[contains(@class, 'main-medium')]") # Информация о заказе
    ORDER_HISTORY = (By.XPATH, "//a[contains(@class, 'OrderHistory_link')]") # Список истории заказов
    IN_PROGRESS = (By.XPATH, "(//ul[contains(@class,'orderList')]/li[contains(@class,'default')])[1]") # Локатор заказов в работе
    GET_PRICE_ORDER = (By.XPATH,"//h2[contains(@class,'title_shadow')]") # Получение цены оформленного заказа
    DONE_ORDERS = (By.XPATH, "(//p[contains(@class,'OrderFeed_number')])[1]") # Выполнено за все время
    DONE_ORDERS_TODAY = (By.XPATH,"(//p[contains(@class,'OrderFeed_number')])[2]") # Выполнено заказов сегодня
    WHOLE_PAGE = (By.XPATH, "(//div[contains(@class, 'Modal_modal_overlay')])[1]") # Вся страница
    CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'close')]") # Закрыть поп ап
    ORDERS_NUMBERS = (By.XPATH, "//li[contains(@class, 'text_type_digits-default')]") # Локатор готового заказа
    GREATE_ORDER = (By.XPATH, "//button[contains(@class, 'button_type_primary' )]") #Оформить заказ
    ORDER_ALL_TIME = (By.XPATH, "//div[contains(@class, 'undefined')]/p[contains(@class, 'OrderFeed_number')]")# Заказов за все время
    ORDER_TODAY = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[2]") #Заказы за день.