import requests
from bs4 import BeautifulSoup

URL = 'https://ru.investing.com/equities/occidental-petro'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.3.848 Yowser/2.5 Safari/537.36', 'accept': '*/*'}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='instrument-header_instrument-header__1SRl8 mb-5 bg-background-surface tablet:grid tablet:grid-cols-2')

    global c_occidental
    crypto = []
    for item in items:
        neg = item.find('span', class_='instrument-price_change-percent__19cas ml-2.5 text-negative-main')
        pos = item.find('span', class_='instrument-price_change-percent__19cas ml-2.5 text-positive-main')
        pr = item.find('span', class_='instrument-price_change-percent__19cas ml-2.5 text-primary')
        if neg:
            z = neg.get_text()
        elif pr:
            z = pr.get_text()
        else:
            z = pos.get_text()

    a = item.find('h1', class_='text-2xl font-semibold instrument-header_title__GTWDv mobile:mb-2').get_text()
    b = item.find('span', class_='text-2xl').get_text()
    c_occidental = (f'{a} | {b} | {z}')
    print(c_occidental)
        #crypto.append({
            #'title': item.find('h1', class_='text-2xl font-semibold instrument-header_title__GTWDv mobile:mb-2').get_text(),
            #'value': item.find('span', class_='text-2xl').get_text(),
            #'volatility': z,
        #})

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')

parse()