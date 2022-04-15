import requests
from bs4 import BeautifulSoup

URL = 'https://www.coingecko.com/ru/Криптовалюты/the-open-network/usd'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.3.848 Yowser/2.5 Safari/537.36', 'accept': '*/*'}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content_ton(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='tw-col-span-2 md:tw-col-span-2')

    global c_ton
    crypto_ton = []
    for item in items:
        neg = item.find('span', class_='text-danger')
        pos = item.find('span', class_='text-green')
        pr = item.find('span', class_='text-danger')
        if neg:
            z = neg.get_text()
        elif pr:
            z = pr.get_text()
        else:
            z = pos.get_text()
    z = z.replace('.',',')
    a = item.find('div', class_='mr-md-3 tw-pl-2 md:tw-mb-0 tw-text-xl tw-font-bold tw-mb-0').get_text().replace('\n', '')
    b = item.find('span', class_='no-wrap').get_text().replace('$', '')
    c_ton = (f'{a} | {b} | ({z})')
    print(c_ton)
        #crypto_ton.append({
            #'title': item.find('div', class_='mr-md-3 tw-pl-2 md:tw-mb-0 tw-text-xl tw-font-bold tw-mb-0').get_text().replace('\n', ''),
            #'value': item.find('span', class_='no-wrap').get_text().replace('$', ''),
            #'volatility': f'({z})'.replace('.',','),
        #})

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content_ton(html.text)
    else:
        print('Error')

parse()