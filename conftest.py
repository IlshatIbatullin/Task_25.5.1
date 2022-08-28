import pytest
import selenium
from selenium.webdriver.common.by import By
from config import valid_email, valid_password


@pytest.fixture(autouse=True)
def login_to_the_page_of_the_tested_site():  # Вход на страницу тестируемого сайта
    pytest.driver = selenium.webdriver.Chrome('/chromedriver.exe')
    pytest.driver.implicitly_wait(5)  # Неявное ожидание загрузки необходимых элементов в течение 5 сек
    pytest.driver.set_window_size(1250, 650)  # Развертывание страницы браузера
    pytest.driver.get('https://petfriends.skillfactory.ru/login')  # Переход на страницу авторизации

    yield

    pytest.driver.quit()  # выход из браузера (прекращение работы вебдрайвера)


@pytest.fixture
def go_to_the_authorization_page():
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element_by_id('email').send_keys(valid_email)  # Ввод email
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element_by_id('pass').send_keys(valid_password)  # Ввод password
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()  # Нажатие на кнопку входа в аккаунт
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element_by_css_selector("a[href='/my_pets']").click()  # Нажатие на ссылку "Мои питомцы"
    pytest.driver.implicitly_wait(5)