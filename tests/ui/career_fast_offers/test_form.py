import allure
import pytest
from models.pages.career_fast_offers_page import career_fast_offers_page


@allure.tag('ui')
@allure.epic('Страница "Быстрые офферы"')
@allure.story('Отправка заявки')
@pytest.mark.ui_test
class TestForm:
    def setup_method(self):
        career_fast_offers_page.open()

    @allure.title('Получение ошибки валидации при пустых полях')
    def test_leave_form_empty(self):
        career_fast_offers_page.leave_form_empty()

        career_fast_offers_page.empty_form_should_have_validation_error()
