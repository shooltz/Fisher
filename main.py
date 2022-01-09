import requests
from typing import Any
from FisherSettings import SETTINGS
import flagman
from loguru import logger


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


@logger.catch
def main():
    html_flagman_main_page = get_html(SETTINGS.HOST)
    if html_flagman_main_page is not None:
        res = flagman.get_catalog(html_flagman_main_page.text)


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
