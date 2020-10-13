import requests
import re
from bs4 import BeautifulSoup

# https://www.elibrary.ru/author_items.asp?authorid=736901&pagenum=1
URL = 'https://elibrary.ru/author_items.asp'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'accept': '*/*'
}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_contet(html):
    soup = BeautifulSoup(html, 'html.parser')
    # извекаем из страницы html таблицу статей
    table = soup.find(id='restab')
    # разбиваем таблицу на каждую статью
    items = table.find_all('tr', {"valign" : "middle"})
    inf = items.pop(0)
    # создаем список статей
    articles = []
    for item in items:
        year = '1'
        if len(re.findall('\d{4}', item.find_all('font').pop().get_text())):
            year = re.findall('\d{4}', item.find_all('font').pop().get_text())[0]
        name = re.sub(r"\r\n", "", item.find('a').get_text())
        name = name[0] + name[1:len(name)].lower()
        articles.append({
            'name': name,
            'authors': re.sub(r"\r\n", "", item.find('i').get_text()).split(','),
            'journal': re.sub(r"\r\n", " ", item.find_all('font').pop().get_text()),
            'year': year
        })
    return articles

def parse(id):
    # 736901
    temp = 1
    res = []
    while True:
        html = get_html(URL, {'authorid': id, 'pagenum': temp})
        if html.status_code == 200:
            page_list = get_contet(html.text)
            if len(page_list) < 1:
                break
            res.extend(page_list)
            temp += 1
        else:
            return 'Error'
    return res