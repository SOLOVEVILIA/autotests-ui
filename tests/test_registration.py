from playwright.sync_api import sync_playwright, Page, expect  # Аннотация
import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
        # Переходим на страницу регистрации
        # Пришлось исправить этот тест тоже, так как он входит в скоуп regression и он падал, после создания компонентов с использованием паттерна PageComponent
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill("user@gmail.com", "username", "password")
        registration_page.registration_form.registration_button.click()
        dashboard_page.dashboard_toolbar.check_visible()