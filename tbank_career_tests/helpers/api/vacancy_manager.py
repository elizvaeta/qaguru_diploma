from random import randrange

from tbank_career_tests.helpers.api_requests import api_request, Method
from tbank_career_tests.models.api.post_vacancies_body import body_default


def find_random_vacancy_id() -> str:
    base_url = 'https://hrsites-api-vacancies.tinkoff.ru/vacancies/public/api/platform'
    url = '/v1/getVacanciesList'
    request_body = body_default

    response = api_request(method=Method.post, url=base_url + url, json=request_body)
    vacancies = response.json()['response']['items'][0]['items']

    vacancies_quantity = len(vacancies)

    return vacancies[randrange(vacancies_quantity)]['id']
