# coding: utf-8

import requests
from bs4 import BeautifulSoup


def convert_phrase(phrase):
    result = ''
    for word in phrase.split(' '):
        result += word + '+'

    return result

def parse_phrase(phrase):

    p = convert_phrase(phrase)


    page = requests.get(f'https://fraze.it/n_search.jsp?q={p}')

    soup = BeautifulSoup(page.content, 'html.parser')


    phrases = soup.findAll("li", {"class": "res_entry"})

    parsed_data = []

    for phrase in phrases:
        title = phrase.find("div", {"class": "qu_txt"}).getText()
        parsed_data.append(title.strip().split('\xa0')[0])

    return parsed_data


