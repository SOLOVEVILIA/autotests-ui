import pytest


@pytest.fixture
def clear_books_database() -> None:
    print("[FIXTURE] Удаляем все данные из БД")

@pytest.fixture
def fill_books_database() -> None:
    print("[FIXTURE] Создаём новые данные из БД")


# Чтобы не передавать фикстуру в аргументы теста (что есть не правильно) и чтобы использовать фикстуры только в определенных теста - используется usefixtures
@pytest.mark.usefixtures("fill_books_database")
def test_read_all_books_in_library():
    print('Reading all books')

# В данном случае, фикстуры будут вызываться для каждой функции и не нужно будет дублировать код (так как scope = functions, по умолчанию)
@pytest.mark.usefixtures(
    "clear_books_database",
    "fill_books_database"
)
class TestLibrary:
    def test_read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...