from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page) # Вызываем super, чтобы вызвать init родительского класса

        # Описываем атрибуты класса / элементы на странице
        self.email_input = page.get_by_test_id("registration-form-email-input").locator('input')
        self.username_input = page.get_by_test_id("registration-form-username-input").locator('input')
        self.password_input = page.get_by_test_id("registration-form-password-input").locator('input')
        self.registration_button = page.get_by_test_id("registration-page-registration-button")

    # Метод заполнения форм с проверкой полей на странице регистрации
    def fill_registration_form(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    # Метод нажатия на кнопку регистрации
    def click_registration_button(self):
        self.registration_button.click()