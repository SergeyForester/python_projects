import requests
from bs4 import BeautifulSoup as bs


def get_results(search_type, beds, baths, min_price, max_price):
    parsed_data = []

    # https://www.realtor.com/realestateandhomes-search/San-Francisco_CA/beds-2/baths-2/price-10-1200000
    # https://www.realtor.com/apartments/San-Francisco_CA/beds-1/baths-1/price-1000-7000
    if search_type == 'buy':
        url = f'https://www.realtor.com/realestateandhomes-search/San-Francisco_CA/beds-{beds}/baths-{baths}/price-{min_price}-{max_price}'
    elif search_type == 'rent':
        url = f'https://www.realtor.com/apartments/San-Francisco_CA/beds-{beds}/baths-{baths}/price-{min_price}-{max_price}'
    else:
        return

    page = requests.get(url)

    soup = bs(page.content, 'html.parser')

    if search_type == 'rent':
        print('scrapping: rent')

        elements = soup.find_all("li", class_="js-component_property-card")
        print(len(elements))

        for el in elements:
            price = el.find("span", {"class": "data-price"}).getText()

            try:
                community = el.find("span", {"class": "listing-community"}).getText()
            except Exception:
                community = ''

            try:
                street = el.find("span", {"class": "listing-street-address"}).getText()
            except Exception:
                street = ''

            try:
                city = el.find("span", {"class": "listing-city"}).getText()
            except Exception:
                city = ''

            location = community + \
                       street + \
                       city

            try:
                size = el.find_all("span", {"class": "data-value"})[-1].getText()
            except Exception as e:
                size = 'No Data'

            link = el.find("a", href=True)['href']

            parsed_data.append({'price': price.strip(), 'size': size.strip(), 'location': location.strip(),
                                'link': f'https://www.realtor.com{link}'})

    elif search_type == 'buy':
        print('scrapping: buy')
        elements = soup.find_all("li", class_="component_property-card")
        print(len(elements))

        for el in elements:

            price = ""
            for tag in el.find("div", {"class": "price"}):
                price += tag.getText()

            location = ''
            for tag in el.find('div', {'class':'address'}):
                location += tag.getText()

            size = ''
            for tag in el.find('ul', {'class':'property-meta'}):
                if tag.attrs.get('data-label') == 'pc-meta-sqft':
                    for i in tag:
                        size += i.getText()

            link = el.find("a", href=True)['href']

            parsed_data.append({'price': price.strip(), 'size': size.strip(), 'location': location.strip(),
                                'link': f'https://www.realtor.com{link}'})


    print(parsed_data)
    print(soup.prettify())
    return parsed_data

# get_results('buy','2','2','0','900000')