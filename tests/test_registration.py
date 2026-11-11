from playwright.sync_api import sync_playwright
import pytest


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration():
    with sync_playwright() as playwright:
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

    # Запускаем ещё один браузер, но вместо явной авторизаии - передаём сформированный json с реквизитами доступа / контекстом
    with sync_playwright() as playwright:
        # Запускаем браузер и открываем новую страницу
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

        # page.wait_for_timeout(5000)
