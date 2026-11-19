from playwright.sync_api import sync_playwright, Page, expect  # Аннотация
import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
        # Переходим на страницу регистрации
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.fill_registration_form("user@gmail.com", "username", "password")
        registration_page.click_registration_button()
        dashboard_page.check_visibility_and_text_dashboard_title()

        # # Ищем локаторы для инпутов и заполняем их данными: почта, имя пользователя, пароль
        # email_input = chromium_page.get_by_test_id("registration-form-email-input").locator('input')
        # email_input.fill("user@gmail.com")
        #
        # username_input = chromium_page.get_by_test_id("registration-form-username-input").locator('input')
        # username_input.fill("username")
        #
        # password_input = chromium_page.get_by_test_id("registration-form-password-input").locator('input')
        # password_input.fill("password")
        #
        # # Ищем локатор для кнопки регистрации и "нажимаем" на неё
        # registration_button = chromium_page.get_by_test_id("registration-page-registration-button")
        # registration_button.click()
        #
        # dashboard_title = chromium_page.get_by_test_id("dashboard-toolbar-title-text")
        # expect(dashboard_title).to_be_visible()