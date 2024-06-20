import allure
import pytest
from tbank_career_tests.models.pages.career_fast_offers_page import career_fast_offers_page
from tbank_career_tests.models.pages.career_it_page import career_it_page
from tbank_career_tests.models.pages.career_page import career_page
from tbank_career_tests.models.pages.menu import menu


@allure.tag('ui')
@allure.epic('Общие компоненты')
@allure.story('Отображение меню')
@pytest.mark.ui_test
class TestMenu:
    @allure.title('Наличие меню на странице "Карьера"')
    def test_career_page_have_menu(self):
        career_page.open()

        menu.should_have_items()

    @allure.title('Наличие меню на странице "Вакансии"')
    def test_career_it_page_have_menu(self):
        career_it_page.open()

        menu.should_have_items()

    @allure.title('Наличие меню на странице "Быстрые офферы"')
    def test_career_fast_offers_page_have_menu(self):
        career_fast_offers_page.open()

        menu.should_have_items()
