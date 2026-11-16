import pytest
from _pytest.fixtures import SubRequest

# Один параметр
@pytest.mark.parametrize(
    'number', [1, 2, 3, -1]
)
def test_numbers(number: int):
    assert number > 0

# Два параметра
@pytest.mark.parametrize(
    'number, expected', [(1, 1), (2,4), (3, 9),]
)
def test_several_numbers(number, expected):
    assert number ** 2 == expected

# "Перемножение" параметров
@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplication_of_numbers(os, browser):
    assert len(os + browser) > 0


# Пример параметризации фикстур
@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request: SubRequest):
    return request.param
# Тест с использованием параметризованной фикстуры
def test_open_browser(browser: str):
    print(f'Running test on browser: {browser}')

# Параметризация класса
@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operation(self, user: str, account: str):
        print(f'User with operation: {user} and account: {account}')

    def test_user_without_operation(self, user: str):
        print(f'User without operation: {user}')

# Тестовые идентификаторы с использованием контекстной функции lambda
users = {
    '+79998881122': 'User with money on bank account',
    '+79998881123': 'User without money on bank account',
    '+79998881124': 'User with operation on bank account',
}

@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
)
def test_identifiers(phone_number):
    ...