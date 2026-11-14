from playwright.sync_api import sync_playwright, Page, Playwright  # Аннотация
import pytest


# Упращение данной фикстуры через использование плагина pytest-playwright
@pytest.fixture # Так как дефолтный scope=function, то не указываем его
def chromium_page(playwright: Playwright) -> Page:
    # Запускаем браузер и открываем новую страницу
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page() # Позволяет вернуть данные до и после теста в pytest, в данном случае return не подойдет
    browser.close()

@pytest.fixture(autouse=False, scope="session")
def initialize_browser_state(playwright: Playwright):
    # Запускаем браузер и открываем новую страницу
    browser = playwright.chromium.launch(headless=False)
    # Задаём контекст (служебная информация для работы бразуера) для сохранения данных из localstorage
    context = browser.new_context()
    page = context.new_page()

    # Переходим на страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Ищем локаторы для инпутов и заполняем их данными: почта, имя пользователя, пароль
    email_input = page.get_by_test_id("registration-form-email-input").locator('input')
    email_input.fill("user@gmail.com")

    username_input = page.get_by_test_id("registration-form-username-input").locator('input')
    username_input.fill("username")

    password_input = page.get_by_test_id("registration-form-password-input").locator('input')
    password_input.fill("password")

    # Ищем локатор для кнопки регистрации и "нажимаем" на неё
    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    # Сохраняем состояние контекста в json файл
    context.storage_state(path='browser-state.json')

    # Закрываем браузер
    browser.close()

@pytest.fixture # scope=function по умолчанию
def chromium_page_with_state(initialize_browser_state,playwright: Playwright) -> Page:
    # Запускаем браузер и открываем новую страницу
    browser = playwright.chromium.launch(headless=False)
    # Передаём контекст, чтобы не авторизовывваться повторно
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    # Переходим на страницу courses
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    yield page

    # Закрываем браузер
    browser.close()