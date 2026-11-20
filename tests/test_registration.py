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