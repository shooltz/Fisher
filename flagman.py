from bs4 import BeautifulSoup, Tag
from typing import Any, List, Union
from urllib.parse import urlparse
from loguru import logger
from my_html_work import get_html


class CatalogItem:
    def __init__(self, name: str, url: urlparse):
        self.name: str = name
        self.url: urlparse = url


class SubCatalogItem:
    def __init__(self, parent: CatalogItem, name: str, url: urlparse):
        self.parent = CatalogItem
        self.name: str = name
        self.url: urlparse = url


def get_catalog(html) -> List[CatalogItem]:
    items: List[CatalogItem] = []
    soup = BeautifulSoup(html, 'html.parser')
    sub_menu = soup.find('div', class_='drop-podmenu_content')
    res = sub_menu.find_all('a', class_='podmenu-title')
    for item in res:
        items.append(CatalogItem(
            name=item.find('div', class_='menuText').get_text(),
            url=item['href']
        ))
    logger.debug(f'It was received {len(items)} categories.')
    return items


def get_sub_categories(item: CatalogItem):
    src = get_html(item.url, )
