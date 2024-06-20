import allure
import pytest
from tbank_career_tests.helpers.api_requests import Method, api_request
from tbank_career_tests.helpers.json_validator import assert_json_schema
from tbank_career_tests.models.api.post_vacancies_body import body_default, body_with_specialties


@allure.tag('api')
@allure.epic('Просмотр списка вакансий')
@pytest.mark.api_test
class TestPostVacanciesList:
    def setup_class(self):
        self.url = '/v1/getVacanciesList'

    @allure.title('Успешный просмотр списка вакансий')
    def test_success(self, base_url):
        request_body = body_default

        response = api_request(method=Method.post, url=base_url + self.url, json=request_body)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body['response']

    @allure.title('Фильтрация по направлению')
    def test_filter_specialties_qa(self, base_url):
        request_body = body_with_specialties

        response = api_request(method=Method.post, url=base_url + self.url, json=request_body)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body['response']['items'][0]['title'] == 'Тестирование'

    @allure.title('Получение ошибки при пустом теле запроса')
    def test_negative_empty_body(self, base_url):
        response = api_request(method=Method.post, url=base_url + self.url)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body['error']['message'] == 'invalid request'
        assert response_body['error']['errcode'] == 'EINVALID'

    @allure.title('Проверка JSON-схемы')
    def test_json_schema(self, base_url):
        request_body = body_default

        response = api_request(method=Method.post, url=base_url + self.url, json=request_body)

        assert_json_schema(response=response, schema_name='vacancies.json')
