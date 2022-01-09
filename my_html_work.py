import time
from typing import Any, Union, Optional
import requests
from loguru import logger
from requests import Response
from FisherSettings import SETTINGS
import random



def get_html(url: str, params='') -> Optional[Response]:
    html: Optional[Response] = None
    try:
        # i = random.randrange(7)
        # logger.debug(f'Sleep in {i}')
        # time.sleep(i)
        html = requests.get(url, params, headers=SETTINGS.HEADERS)
        if html.status_code != requests.codes.ok:
            raise requests.HTTPError
        logger.debug(f'The {url} page of flagman.kiev.ua was received. ')
    except requests.HTTPError as e:
        logger.error(e)
    return html
