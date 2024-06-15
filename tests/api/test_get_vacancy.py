import pytest
from faker import Faker
from helpers.api.vacancy_manager import find_random_vacancy_id
from helpers.api_requests import api_get
from helpers.json_validator import assert_json_schema


@pytest.mark.api_test
class TestPostVacanciesList:
    def setup_class(self):
        self.url = '/v2/getVacancy'

        self.url_slug = find_random_vacancy_id()

    def test_success(self):
        params = {
            'urlSlug': self.url_slug
        }

        response = api_get(url=self.url, params=params)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body['response']

    def test_negative_random_url_slug(self):
        params = {
            'urlSlug': Faker().word()
        }

        response = api_get(url=self.url, params=params)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body['error']['message'] == 'Vacancy not found'
        assert response_body['error']['errcode'] == 'ENOTFOUND'

    def test_json_schema(self):
        params = {
            'urlSlug': self.url_slug
        }

        response = api_get(url=self.url, params=params)

        assert_json_schema(response=response, schema_name='vacancy.json')
