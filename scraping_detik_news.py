import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})
soup = BeautifulSoup(req.text, 'html.parser')
popular_area = soup.find(attrs={'class': 'grid-row list-content'})
content_item = popular_area.find_all(attrs={'class': 'list-content__item'})

for index in content_item:
    print(f"image : {index.find('a').find('img')}")
    print(f"title : {index.find_all(attrs={'class': 'media__title'})[0].find('a').text}")
    print(f"href : {index.find_all(attrs={'class': 'media__title'})[0].find('a')['href']}")
