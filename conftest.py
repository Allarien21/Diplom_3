import pytest
import urls

from selenium import webdriver
from data import CreateUser
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    if request.param == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--window-size=1200,1000")
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == "firefox":
        firefox_options = Options()
        firefox_options.add_argument("--width=1200")
        firefox_options.add_argument("--height=1000")
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise ValueError("Ошибка драйвера")
    driver.get(urls.API_HOST)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def user_credentials():
    user_data = CreateUser.generate_new_user_credentials()
    user = CreateUser.registration_user(user_data)
    yield user
    CreateUser.delete_user(user['accessToken'])