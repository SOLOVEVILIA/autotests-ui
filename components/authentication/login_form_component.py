from playwright.sync_api import Page

from components.base_component import BaseComponent, expect


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page) # Вызываем super, чтобы вызвать init родительского класса

        # Описываем атрибуты класса / элементы на странице
        self.email_input = page.get_by_test_id("login-form-email-input").locator('input')
        self.password_input = page.get_by_test_id("login-form-password-input").locator('input')
        self.login_button = page.get_by_test_id("login-page-login-button")

    # Метод заполнения форм с проверкой полей
    def fill(self, email: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    # Проверка алерта при невалидных данных
    def check_visible(self, email: str, password: str):
        expect(self.email_input).to_be_visible()
        expect(self.email_input).to_have_value(email)
        expect(self.password_input).to_be_visible()
        expect(self.password_input).to_have_value(password)
        expect(self.login_button).to_be_visible()
