from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Запускаем браузер и открываем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Ищем локаторы для инпутов и заполняем их данными: почта, имя пользователя, пароль
    email_input = page.get_by_test_id("registration-form-email-input").locator('input')
    email_input.fill("user.name@gmail.com")

    username_input = page.get_by_test_id("registration-form-username-input").locator('input')
    username_input.fill("username")

    password_input = page.get_by_test_id("registration-form-password-input").locator('input')
    password_input.fill("password")

    # Ищем локатор для кнопки регистрации и "нажимаем" на неё
    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    # Объявляем переменную для заголовка Dashboard
    dashboard_check = page.get_by_test_id("dashboard-toolbar-title-text")
    # Добавляем ожидаемый результат: найденный заголовок видим и содержит текст с названием раздела
    expect(dashboard_check).to_be_visible()
    expect(dashboard_check).to_have_text("Dashboard")

    # Отладочная функция ожидания в 5 секунд
    # page.wait_for_timeout(5000)