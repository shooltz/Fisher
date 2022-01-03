from bs4 import BeautifulSoup
import urllib.request

url_flagman_rods: str = 'https://www.flagman.kiev.ua/udilishcha/c166335/'
page = urllib.request.urlopen(url_flagman_rods)


soup = BeautifulSoup(page, 'html.parser')
all_rods_category = soup.find_all(class_='title')
for i in all_rods_category:
	res = i.find('a', href=True).get('href')
	print(res)
# print(page.status_code)
# print(all_rods_category)
