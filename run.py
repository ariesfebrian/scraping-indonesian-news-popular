import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/detik-popular')
def detik_popular():
    html_doc = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    popular_area = soup.find(attrs={'class': 'grid-row list-content'})
    content_item = popular_area.find_all(attrs={'class': 'list-content__item'})

    return render_template('detik-scraping.html', content_item=content_item)


@app.route('/kompas-popular')
def kompas_popular():
    html_doc = requests.get('https://indeks.kompas.com/terpopuler')
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    popular_area = soup.find(attrs={'class': 'latest--indeks'})
    if popular_area is None:
        content_item = 'None'
    else:
        content_item = popular_area.find_all(attrs={'class': 'article__list'})
    print(content_item)
    return render_template('kompas-scraping.html', content_item=content_item)


@app.route('/tempo-popular')
def tempo_popular():
    html_doc = requests.get('https://www.tempo.co/populer')
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    popular_area = soup.find(attrs={'class': 'list list-type-1'})
    content_item = popular_area.find_all(attrs={'class': 'card card-type-1'})

    return render_template('tempo-scraping.html', content_item=content_item)


if __name__ == '__main__':
    app.run(debug=True)
