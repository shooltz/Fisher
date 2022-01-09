import requests
from typing import Any, List
from FisherSettings import SETTINGS
import flagman
from loguru import logger
from os import system

from my_html_work import get_html


@logger.catch
def main():
    logger.add('fisher.log', rotation="100 MB")
    logger.info('The script started.')
    html_flagman_main_page = get_html(SETTINGS.HOST)
    if html_flagman_main_page is None:
        logger.error('No html was received.')
        Exception('No html was received.')
    categories_list: List[flagman.Category] = flagman.get_catalog(html_flagman_main_page.text)
    if categories_list is None:
        logger.error('No categories was received.')
        Exception('No html was received.')
    subcategories_list = flagman.Categories()
    for item in categories_list:
        pass
        #todo subcategories_list.exapnd(flagman.get_sub_categories(item))
    pass
    logger.info('Script stop')


if __name__ == "__main__":
    main()

# url_flagman_rods: str = 'https://www.flagman.kiev.ua/udilishcha/c166335/'
# page: Any = urllib.request.urlopen(url_flagman_rods)
#
#
# soup: Any = BeautifulSoup(page, 'html.parser')
# all_rods_category = soup.find_all(class_='title')
# for i in all_rods_category:
# 	res = i.find('a', href=True).get('href')
# 	print(res)
# # print(page.status_code)
# # print(all_rods_category)
