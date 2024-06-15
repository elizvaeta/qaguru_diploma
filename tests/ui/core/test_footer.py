import allure
import pytest
from models.pages.career_fast_offers_page import career_fast_offers_page
from models.pages.career_it_page import career_it_page
from models.pages.career_page import career_page
from models.pages.footer import footer


@allure.tag('ui')
@allure.epic('Общие компоненты')
@allure.story('Отображение футера')
@pytest.mark.ui_test
class TestFooter:
    @allure.title('Наличие соц. сетей в футере на странице "Карьера"')
    def test_career_page_have_social_medias(self):
        career_page.open()

        footer.should_have_social_medias()

    @allure.title('Наличие соц. сетей в футере на странице "Вакансии"')
    def test_career_it_page_have_social_medias(self):
        career_it_page.open()

        footer.should_have_social_medias()

    @allure.title('Наличие соц. сетей в футере на странице "Быстрые офферы"')
    def test_career_fast_offers_page_have_social_medias(self):
        career_fast_offers_page.open()

        footer.should_have_social_medias()
