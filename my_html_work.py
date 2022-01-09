import requests
from typing import Any
from loguru import logger
from FisherSettings import SETTINGS


def get_html(url: str, params='') -> Any:
    html: Any = None
    try:
        html = requests.get(url, params, headers=SETTINGS.HEADERS)
        if html.status_code != requests.codes.ok:
            raise requests.HTTPError
        logger.debug('The main page of flagman.kiev.ua was received. ')
    except requests.HTTPError as e:
        logger.error(e)
    return html
