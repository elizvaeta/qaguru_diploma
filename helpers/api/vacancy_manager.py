from random import randrange

from helpers.api_requests import api_post
from models.api.post_vacancies_body import body_default


def find_random_vacancy_id() -> str:
    url = '/v1/getVacanciesList'
    request_body = body_default

    response = api_post(url=url, json=request_body)
    vacancies = response.json()['response']['items'][0]['items']

    vacancies_quantity = len(vacancies)

    return vacancies[randrange(vacancies_quantity)]['id']
