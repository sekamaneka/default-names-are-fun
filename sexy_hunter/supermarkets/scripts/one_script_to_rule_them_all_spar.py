from bs4 import BeautifulSoup
import requests


def get_all_spar_items():
    monatssparer = requests.get(
        'http://www.spar.at/de_AT/index/aktionen/Monatssparer.html')
    plus = requests.get(
        'http://www.spar.at/de_AT/index/aktionen/1-1-gratis-aktionen.html')
    sparangebote = requests.get(
        'http://www.spar.at/de_AT/index/aktionen/SPARAngebote.html')
    sites = [monatssparer, plus, sparangebote]
    item_dictionary = list(dict())
    for link in sites:
        soup = BeautifulSoup(link.text)
        for items in soup.find_all('div', class_='socialMediaStart'):
            title = items.find('input', class_='socialMediaTitle')
            img = items.find('input', class_='socialMediaImage')
            link = items.find('input', class_='socialMediaLink')
            text = items.find('div', class_='action-offer')
            price = items.find('p', class_='action-preises')
            if text:
                price = price.get_text()[:-2]+'.'+price.get_text()[-2:]
                item_dictionary.append({'name': title['value'],
                                        'img': img['value'],
                                        'link': link['value'],
                                        'old_price': text.get_text().split()[-1],
                                        'new_price': price})
    return item_dictionary
