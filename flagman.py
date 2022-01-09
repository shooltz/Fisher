from bs4 import BeautifulSoup, Tag
from typing import List
from urllib.parse import urlparse
from loguru import logger
from my_html_work import get_html


class Category:
    def __init__(self, name: str, url: urlparse):
        self.name: str = name
        self.url: urlparse = url

    def __str__(self):
        return '%s - %s' % (self.name, self.url)


class Categories:
    def __init__(self):
        self.list: List[Category] = []

    def add_category(self, category: Category) -> None:
        self.list.append(category)


    # todo add expand method


def get_catalog(html) -> List[Category]:
    items: List[Category] = []
    soup = BeautifulSoup(html, 'html.parser')
    sub_menu: Tag = soup.find('div', class_='drop-podmenu_content')
    res: List[str] = sub_menu.find_all('a', class_='podmenu-title')
    for item in res:
        items.append(Category(
            name=item.find('div', class_='menuText').get_text(),
            url=item['href']
        ))
    logger.debug(f'It was received {len(items)} categories.')
    return items


def get_sub_categories(item: Category) -> Categories:
    src = get_html(item.url, '')
    categories = Categories()
    soup = BeautifulSoup(src.text, 'html.parser')
    try:
        subcategories_list = soup.find('div', {'class': 'row', 'data-page-type': 'categories'}).find_all('div',
                                                                                                         class_='title')
    except AttributeError as e:
        logger.debug(f"{item.name} - {item.url} hasn't got subcategories.")
        categories.add_category(item)
    else:
        for item in subcategories_list:
            url = item.a['href']
            name = item.a.get_text()
            logger.debug(f'{name} - {url}')
            categories.add_category(Category(name, url))
    return categories
