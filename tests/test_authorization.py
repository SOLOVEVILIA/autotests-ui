from playwright.sync_api import expect, Page
import pytest

@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize(
        'email, password',
        [
                ("user.name@gmail.com", "password"),
                ("user.name@gmail.com", "  "),
                (" ", "password")
        ]
)
def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str):
        # Переходим на указанную страицу
        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        # Ищем локаторы для инпутов и заполняем их данными
        email_input = chromium_page.get_by_test_id("login-form-email-input").locator('input')
        email_input.fill(email)

        password_input = chromium_page.get_by_test_id("login-form-password-input").locator('input')
        password_input.fill(password)

        # Ищем локатор для кнопки и "нажимаем" на неё
        login_button = chromium_page.get_by_test_id("login-page-login-button")
        login_button.click()

        # Ищем ошибку (так как реквизиты некорректны, должна появиться плашка с ошибкой)
        wrong_email_or_password_alert = chromium_page.get_by_test_id("login-page-wrong-email-or-password-alert")
        # Добавляем ожидаемый результат: найденный локатор видим и содержит текст с ошибкой
        expect(wrong_email_or_password_alert).to_be_visible()
        expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")