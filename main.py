from bs4 import BeautifulSoup
import requests
from typing import Any, Dict
from FisherSettings import SETTINGS
import flagman


def get_html(url: str, params='') -> Any:
    html = requests.get(url, params, headers=SETTINGS.HEADERS)
    return html


r = get_html(SETTINGS.HOST)
menu = flagman.get_drop_menu(r.text)
res = flagman.get_catalog(menu)
print(res)



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
