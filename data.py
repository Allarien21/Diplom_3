import random
import string
import requests
import allure

import urls

INGREDIENT_DETAILS = 'Детали ингредиента'
GRATE_ORDER = 'идентификатор заказа'
DONE_ORDER = 'Выполнен'
CONSTRUCTOR = 'Соберите бургер'
FEED_ORDER = 'Лента заказов'
INFO_ORDER = 'Cостав'


class CreateUser:
    @staticmethod
    @allure.step("Генерация данных для регистрации")
    def generate_new_user_credentials():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for _ in range(length))
            return random_string

        def generate_email():
            username = generate_random_string(7)  # Генерируем имя пользователя длиной 7 символов
            domain = generate_random_string(5)  # Генерируем доменное имя длиной 5 символов
            email = f"{username}@{domain}.com"  # Собираем email в формате username@domain.com
            return email

        email = generate_email()
        password = generate_random_string(10)
        name = generate_random_string(10)

        credentials = {
            "email": email,
            "password": password,
            "name": name
        }
        return credentials

    @allure.title('Создание пользователя')
    @staticmethod
    def registration_user(credentials):
        response = requests.post(urls.USER_REGISTER, data=credentials)
        if response.status_code == 200:
            response_body = response.json()
            access_token = response_body.get('accessToken')
            return {
                'name':credentials['name'],
                'email': credentials['email'],
                'password': credentials['password'],
                'accessToken': access_token
            }
        else:
            raise Exception(f"Ошибка при создании пользователя: {response.status_code} - {response.text}")

    @allure.title('Удаление пользователя')
    @staticmethod
    def delete_user(access_token):
        requests.delete(urls.USER_DELETE, headers={'Authorization': access_token})