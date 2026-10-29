from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Запускаем браузер и открываем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Находим кнопку
    registration_button = page.get_by_test_id("registration-page-registration-button")
    # Проверям, что по умолчанию, кнопка задизейблена
    expect(registration_button).to_be_disabled()

    # Ищем локаторы для инпутов и заполняем их данными: почта, имя пользователя, пароль
    email_input = page.get_by_test_id("registration-form-email-input").locator('input')
    email_input.fill("user.name@gmail.com")

    username_input = page.get_by_test_id("registration-form-username-input").locator('input')
    username_input.fill("username")

    password_input = page.get_by_test_id("registration-form-password-input").locator('input')
    password_input.fill("password")

    # Проверям, что кнопка стала активна
    expect(registration_button).to_be_enabled()

    # Отладочная функция: ожидание в 5 секунд
    # page.wait_for_timeout(5000)