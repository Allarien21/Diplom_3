from selenium.webdriver.common.by import By

class Main:
    PERSONAL_ACC = (By.XPATH, "//a[@href='/account']")  # Кнопка Личного кабинета
    CONSTRUCTOR = (By.XPATH, "(//p[contains(@Class, 'AppHeader_header')])[1]")  # Кнопка Конструктора
    ASSEMBLE_BURGER = (By.XPATH, "//section[contains(@class, 'ingredients')]/h1[contains(@class ,'type_main')]")  # локатор "Соберите Заказ"


    ORDER_FEED = (By.XPATH, "//a[@href='/feed']")  # Кнопка Лента заказов
    FEED_ORDER_TEXT = (By.XPATH,"//div[contains(@class ,'OrderFeed' )]/h1[contains(@class,'type_main')]") # локатор "Лента заказов"

    INGREDIENT = (By.XPATH,"(//a[contains(@class,'BurgerIngredient')]/img[contains(@class,'ingredient__image')])[1]") # Первый ингридиент из списка
    ORDER_BASKET = (By.XPATH, "(//section[contains(@class, 'BurgerConstructor_basket')]//li)[1]") # Локатор "корзины"
    COUNTER = (By.XPATH,".//a[@href= '/ingredient/61c0c5a71d1f82001bdaaa6d']/div/p[contains(@class, 'counter')]")  # Кол-во ингридиента в "корзине"

    INGREDIENT_DETAIL = (By.XPATH,"(//div[contains(@class ,'Modal_modal')]/h2[contains(@class,'Modal_modal')])[1]") # Локатор Деталей ингрииента
    CLOSE = (By.XPATH,"//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'close')]") # Крестик окна Детали заказа
    WINDOW_INFO_INGREDIENT = (By.XPATH,"(//section[contains(@class,'Modal_modal')])[1]") # Окно Деталей ингрииента
    PLACE_ORDER = (By.XPATH, "//button[contains(@class, 'button')]")  # Кнопка Оформление заказа

    GRATE_ORDER = (By.XPATH, "//div[contains(@class,'contentBox')]/p[contains(@class ,'undefined')]")  # Поп ап оформленного заказа
