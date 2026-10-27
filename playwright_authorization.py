from playwright.sync_api import sync_playwright, expect
# Контекстный менеджер
with sync_playwright() as playwright:
    # Запускаем браузер и открываем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на указанную страицу
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Ищем локаторы для инпутов и заполняем их данными
    email_input = page.get_by_test_id("login-form-email-input").locator('input')
    email_input.fill("user.name@gmail.com")

    password_input = page.get_by_test_id("login-form-password-input").locator('input')
    password_input.fill("password")

    # Ищем локатор для кнопки и "нажимаем" на неё
    login_button = page.get_by_test_id("login-page-login-button")
    login_button.click()

    # Ищем ошибку (так как реквизиты некорректны, должна появиться плашка с ошибкой)
    wrong_email_or_password_alert = page.get_by_test_id("login-page-wrong-email-or-password-alert")
    # Добавляем ожидаемый результат: найденный локатор видим и содержит текст с ошибкой
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")

    # page.wait_for_timeout(5000)