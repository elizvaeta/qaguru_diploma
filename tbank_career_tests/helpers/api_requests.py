from enum import Enum

import allure
import requests
from tbank_career_tests.helpers.logger import log_response


class Method(Enum):
    get = 'GET'
    post = 'POST'


def api_request(method: Method, url: str, **kwargs) -> requests.Response:
    url = url

    with allure.step('Отправка запроса'):
        response = requests.request(method=method.value, url=url, timeout=120, **kwargs)

    log_response(response=response, method='GET')

    return response
