from playwright.sync_api import sync_playwright, Page, expect  # Аннотация
import pytest


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page):
        # Переходим на страницу регистрации
        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Ищем локаторы для инпутов и заполняем их данными: почта, имя пользователя, пароль
        email_input = chromium_page.get_by_test_id("registration-form-email-input").locator('input')
        email_input.fill("user@gmail.com")

        username_input = chromium_page.get_by_test_id("registration-form-username-input").locator('input')
        username_input.fill("username")

        password_input = chromium_page.get_by_test_id("registration-form-password-input").locator('input')
        password_input.fill("password")

        # Ищем локатор для кнопки регистрации и "нажимаем" на неё
        registration_button = chromium_page.get_by_test_id("registration-page-registration-button")
        registration_button.click()

        dashboard_title = chromium_page.get_by_test_id("dashboard-toolbar-title-text")
        expect(dashboard_title).to_be_visible()