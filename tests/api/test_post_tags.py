import allure
import pytest
from tbank_career_tests.helpers.api_requests import api_request, Method
from tbank_career_tests.helpers.json_validator import assert_json_schema
from tbank_career_tests.models.api.post_tags_body import body_with_specialties, body_default


@allure.tag('api')
@allure.epic('Просмотр списка тегов')
@pytest.mark.api_test
class TestPostTags:
    def setup_class(self):
        self.url = '/v1/getTags'

    @allure.title('Успешный просмотр списка тегов')
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
        assert not response_body['response']

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

        assert_json_schema(response=response, schema_name='tags.json')
