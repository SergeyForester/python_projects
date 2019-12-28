# coding: utf-8

import requests
from bs4 import BeautifulSoup


# url = f'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&maxprice=10000000&offer_type=flat&region=1&room1=1&room2=1'

def create_link(params):
    # {'deal_type':'sale', 'maxprice':'10000000'} etc.
    url = f'https://www.cian.ru/cat.php?'

    for key, value in params.items():
        url += f'{key}={value}&'

    return url


def parse(params):
    url = create_link(params)

    page = requests.get(url)

    print(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.findAll("div", {"class": "c6e8ba5398--container--Y5gG9"})

    parsed_data = []

    for result in results:
        link = result.find("a", {"class": "c6e8ba5398--header--1fV2A"}, href=True)['href']

        underground = result.find("div", {"class": "c6e8ba5398--underground-name--1efZ3"}).getText()

        try:
            title = result.find("div", {"class": "c6e8ba5398--subtitle--UTwbQ"}).getText()
        except AttributeError:
            title = result.find("div", {"class": "c6e8ba5398--single_title--22TGT"}).getText()

        price = result.find("div", {"class": "c6e8ba5398--header--1dF9r"}).getText()

        parsed_data.append({'title': title, 'price': price, 'underground': underground, 'link': link})

    return parsed_data


for res in parse({'maxprice': '1000000', 'region': '1'}):
    print(res)
