from playwright.sync_api import sync_playwright, expect
import pytest


# Добавлены декораторы
@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    # Объявляем переменную для заголовка Courses
    courses_check = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    # Добавляем ожидаемый результат: найденный заголовок видим и содержит текст с названием раздела
    expect(courses_check).to_be_visible()
    expect(courses_check).to_have_text("Courses")

    # Проверяем текст блока "There is no results"
    text_check = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(text_check).to_be_visible()
    expect(text_check).to_have_text("There is no results")

    # Проверяем видимость иконки пустого блока
    icon_check = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(icon_check).to_be_visible()

    # Проверяем наличие и видимость блока: "Results from the load test pipeline will be displayed here"
    text_description_check = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(text_description_check).to_be_visible()
    expect(text_description_check).to_have_text("Results from the load test pipeline will be displayed here")