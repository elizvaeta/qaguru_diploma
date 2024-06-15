import allure
import pytest
from models.pages.career_page import career_page


@allure.tag('ui')
@allure.epic('Страница "Карьера"')
@allure.story('Отображение контента')
@pytest.mark.ui_test
class TestPageContains:
    def setup_method(self):
        career_page.open()

    @allure.title('Наличие информационных блоков')
    def test_have_info_blocks(self):
        career_page.should_have_info_blocks()

    @allure.title('Переход к списку вакансий')
    def test_go_to_vacancies(self):
        career_page.should_go_to_vacancies()

    @allure.title('Переход в блог')
    def test_go_to_blog(self):
        career_page.should_go_to_blog()
