from time import clock_settime

import pytest


@pytest.fixture(autouse=True) # Автоматический запуск перед тестом
def send_analytics_data():
    print('[AUTOUSE] Отправляем данные в сервис аналитики')

@pytest.fixture(scope="session") # Масштаб запуска = один раз на тестовую сессию
def settings():
    print('[SESSION] Инициализируем настройки автотестов')

@pytest.fixture(scope="class") # Масштаб запуска = один раз на тестовый класс
def user():
    print('[CLASS] Создаём данные пользователя один раз на тестовый класс')

@pytest.fixture(scope="function") # Масштаб запуска = один раз на тестовую функцию
def browser():
    print('[FUNCTION] Отркываем браузер на каждый автотест')


# В классе передаём созданные фикстуры в аргумент функций
class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        ...

    def test_user_can_create_course(self, settings, user, browser):
        ...

class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        ...