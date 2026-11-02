from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Запускаем браузер и открываем новую страницу
    browser = playwright.chromium.launch(headless=False)
    # Задаём контекст (служебная информация для работы бразуера) для сохранения данных из localstorage
    context = browser.new_context()
    page = context.new_page()

    # Переходим на страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Ищем локаторы для инпутов и заполняем их данными: почта, имя пользователя, пароль
    email_input = page.get_by_test_id("registration-form-email-input").locator('input')
    email_input.fill("user@gmail.com")

    username_input = page.get_by_test_id("registration-form-username-input").locator('input')
    username_input.fill("username")

    password_input = page.get_by_test_id("registration-form-password-input").locator('input')
    password_input.fill("password")

    # Ищем локатор для кнопки регистрации и "нажимаем" на неё
    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    # Сохраняем состояние контекста в json файл
    context.storage_state(path='browser-state.json')

# Запускаем браузер повторно
with sync_playwright() as playwright:
    # Запускаем браузер и открываем новую страницу
    browser = playwright.chromium.launch(headless=False)
    # Передаём контекст, чтобы не авторизовывваться повторно
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    # Сразу переходим на страницу courses
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Объявляем переменную для заголовка Courses
    courses_check = page.get_by_test_id("courses-list-toolbar-title-text")
    # Добавляем ожидаемый результат: найденный заголовок видим и содержит текст с названием раздела
    expect(courses_check).to_be_visible()
    expect(courses_check).to_have_text("Courses")

    # Проверяем текст блока "There is no results"
    text_check = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(text_check).to_be_visible()
    expect(text_check).to_have_text("There is no results")

    # Проверяем видимость иконки пустого блока
    icon_check = page.get_by_test_id("courses-list-empty-view-icon")
    expect(icon_check).to_be_visible()

    # Проверяем наличие и видимость блока: "Results from the load test pipeline will be displayed here"
    text_description_check = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(text_description_check).to_be_visible()
    expect(text_description_check).to_have_text("Results from the load test pipeline will be displayed here")

    # page.wait_for_timeout(5000)
