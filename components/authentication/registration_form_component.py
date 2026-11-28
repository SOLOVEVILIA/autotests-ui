from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        # Описываем атрибуты класса / элементы на странице
        self.email_input = page.get_by_test_id("registration-form-email-input").locator('input')
        self.username_input = page.get_by_test_id("registration-form-username-input").locator('input')
        self.password_input = page.get_by_test_id("registration-form-password-input").locator('input')
        self.registration_button = page.get_by_test_id("registration-page-registration-button")

    # Метод заполнения форм с проверкой полей на странице регистрации
    def fill(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    # Метод проверки видимости полей и наличия значений
    def click_visible(self, email: str, username: str, password: str):
        expect(self.email_input).to_be_visible()
        expect(self.email_input).to_have_value(email)
        expect(self.username_input).to_be_visible()
        expect(self.username_input).to_have_value(username)
        expect(self.password_input).to_be_visible()
        expect(self.password_input).to_have_value(password)
        expect(self.registration_button).to_be_visible()