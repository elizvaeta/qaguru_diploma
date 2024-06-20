import allure
import pytest
from faker import Faker
from tbank_career_tests.helpers.api.vacancy_manager import find_random_vacancy_id
from tbank_career_tests.helpers.api_requests import api_request, Method
from tbank_career_tests.helpers.json_validator import assert_json_schema


@allure.tag('api')
@allure.epic('Просмотр вакансии')
@pytest.mark.api_test
class TestGetVacancy:
    def setup_class(self):
        self.url = '/v2/getVacancy'

        self.url_slug = find_random_vacancy_id()

    @allure.title('Успешный просмотр вакансии')
    def test_success(self, base_url):
        params = {
            'urlSlug': self.url_slug
        }

        response = api_request(method=Method.get, url=base_url + self.url, params=params)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body['response']

    @allure.title('Получение ошибки при просмотре несуществующей вакансии')
    def test_negative_random_url_slug(self, base_url):
        params = {
            'urlSlug': Faker().word()
        }

        response = api_request(method=Method.get, url=base_url + self.url, params=params)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body['error']['message'] == 'Vacancy not found'
        assert response_body['error']['errcode'] == 'ENOTFOUND'

    @allure.title('Проверка JSON-схемы')
    def test_json_schema(self, base_url):
        params = {
            'urlSlug': self.url_slug
        }

        response = api_request(method=Method.get, url=base_url + self.url, params=params)

        assert_json_schema(response=response, schema_name='vacancy.json')
