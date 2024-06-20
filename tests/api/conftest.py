import pytest


@pytest.fixture(scope='function')
def base_url():
    base_url = 'https://hrsites-api-vacancies.tinkoff.ru/vacancies/public/api/platform'
    return base_url
