from playwright.sync_api import sync_playwright, Request, Response

# Объявляем функцию для сбора логов запросов
def log_request(request: Request):
    print(f'Request: {request.url}')

# Объявляем функцию для сбора логов ответов
def log_response(response: Response):
    print(f'Response: {response.url}, {response.status}')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на указанную страицу и ждём полную загрузку страницы
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
    )

    # Вызываем обработчик событий для наших функций
    page.on('request', log_request)
    page.on('response', log_response)

    page.wait_for_timeout(5000)