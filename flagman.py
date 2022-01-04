from bs4 import BeautifulSoup, Tag
from typing import Any, List, Union
from urllib.parse import urlparse


class CatalogItem:
    def __init__(self, name: str, url: urlparse):
        self.name: str = name
        self.url: urlparse = url


def get_drop_menu(html) -> Union[Tag]:
    soup = BeautifulSoup(html, 'html.parser')
    drop_menu = soup.find('div', class_='drop-podmenu_content')
    return drop_menu


def get_catalog(html) -> List[CatalogItem]:
    items: List[CatalogItem] = []
    soup = BeautifulSoup(html, 'html.parser')
    columns = soup.find_all('li')
    for column in columns:
        items = column.find_all('a', class_='podmenu-title')
        for item in items:
            item_menu = CatalogItem(
                name=item.find('div', class_='menuText').get_text(),
                url=item.find('a', class_='podmenu-title').get('href')
            )
            print(item)
    return items
