import allure
import requests
from helpers.logger import log_response
from tests.api.conftest import BASE_URL


def api_get(url: str, **kwargs) -> requests.Response:
    url = BASE_URL + url

    with allure.step('Отправка запроса'):
        response = requests.get(url=url, timeout=120, **kwargs)

    log_response(response=response, method='GET')

    return response


def api_post(url: str, **kwargs) -> requests.Response:
    url = BASE_URL + url

    with allure.step('Отправка запроса'):
        response = requests.post(url=url, timeout=120, **kwargs)

    log_response(response=response, method='POST')

    return response
