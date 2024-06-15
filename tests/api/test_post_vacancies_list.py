import pytest
from helpers.api_requests import api_post
from helpers.json_validator import assert_json_schema
from models.api.post_vacancies_body import body_default, body_with_specialties


@pytest.mark.api_test
class TestPostVacanciesList:
    def setup_class(self):
        self.url = '/v1/getVacanciesList'

    def test_success(self):
        request_body = body_default

        response = api_post(url=self.url, json=request_body)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body['response']

    def test_filter_specialties_qa(self):
        request_body = body_with_specialties

        response = api_post(url=self.url, json=request_body)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body['response']['items'][0]['title'] == 'Тестирование'

    def test_negative_empty_body(self):
        response = api_post(url=self.url)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body['error']['message'] == 'invalid request'
        assert response_body['error']['errcode'] == 'EINVALID'

    def test_json_schema(self):
        request_body = body_default

        response = api_post(url=self.url, json=request_body)

        assert_json_schema(response=response, schema_name='vacancies.json')
