from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на указанную страицу и ждём полную загрузку страницы
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
        wait_until="networkidle"
    )

    # Переменная для передачи в js
    new_text = "New Text"

    # Вызываем метод, который позволяет запускать js код через playwright и передаём js код (безымянная функция)
    page.evaluate(
        """
        (text) => {
            const title = document.getElementById('authentication-ui-course-title-text')
            title.textContent = text
        }
        """,
        new_text
    )

    page.wait_for_timeout(5000)