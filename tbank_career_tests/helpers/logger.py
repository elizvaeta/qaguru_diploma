import logging

from requests import Response


def log_response(response: Response, method: str) -> None:
    logging.info(
        f'\nЭндпоинт: {method} {response.request.url}\n'
        f'Тело запроса: {response.request.body}\n'
        f'Статус ответа: {response.status_code}\n'
        f'Тело ответа: {response.text}\n'
    )
