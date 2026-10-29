from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на указанную страицу
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Ищем локаторы для инпутов и ставим фокус на инпут
    email_input = page.get_by_test_id("login-form-email-input").locator('input')
    email_input.focus()

    # Теперь можно "печатать" с кливиатуры (с задержкой между вводом каждого символа)
    for char in "user.name@gmail.com":
        page.keyboard.type(char, delay=300)

    # Выделяем полученный текст
    page.keyboard.press("ControlOrMeta+A")

    page.wait_for_timeout(5000)