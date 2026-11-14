from playwright.sync_api import sync_playwright, Page, Playwright  # Аннотация
import pytest

# Упращение данной фикстуры через использование плагина pytest-playwright
@pytest.fixture # Так как дефолтный scope=function, то не указываем его
def chromium_page(playwright: Playwright) -> Page:
    # Запускаем браузер и открываем новую страницу
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page() # Позволяет вернуть данные до и после теста в pytest, в данном случае return не подойдет
    browser.close()