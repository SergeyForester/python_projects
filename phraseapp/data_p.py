# coding: utf-8

import requests
from bs4 import BeautifulSoup


def convert_phrase(phrase):
    result = ''
    for word in phrase.split(' '):
        result += word + '+'

    return result


def parse_phrase(phrase, key=None):
    try:
        p = convert_phrase(phrase)

        if not key:  # if language is English
            url = f'https://fraze.it/n_search.jsp?q={p}'
        else:
            url = f'https://fraze.it/n_search.jsp?q={p}&l={key}'

        page = requests.get(url)

        print(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        phrases = soup.findAll("li", {"class": "res_entry"})

        parsed_data = []

        for phrase in phrases:
            title = phrase.find("div", {"class": "qu_txt"}).getText()
            parsed_data.append(title.strip().split('\xa0')[0])

        return parsed_data
    except:
        return []
