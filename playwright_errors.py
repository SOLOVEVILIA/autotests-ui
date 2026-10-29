from playwright.sync_api import sync_playwright, Request, Response, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на указанную страицу и ждём полную загрузку страницы
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
    )

    # Пытаемся найти неизвестный локатор
    # unknown = page.locator('#unknown')
    # expect(unknown).to_be_visible(

    # Пытаемся ввести текст в кнопку Login
    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('unknown')

    # Пытаемся изменить текст заголовка у которого title = none,
    # так как он не успел загрузиться (не добавляли ожидания завершения сетевых запросов)
    page.evaluate(
        """
          const title = document.getElementById('authentication-ui-course-title-text');
          title.textContent = 'New Text';
        """
    )