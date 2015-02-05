import os
from fetcher import main
import django
from django.conf import settings
import json
def add_items(supermarket, i_name, menge, inhalt, aktion_price, normal_price, aktion_grundpreis, category, aktion):
    c = Item.objects.get_or_create(supermarket=supermarket, i_name=i_name,
            menge = menge, inhalt = inhalt,
            aktion_price=aktion_price, normal_price=normal_price,
            aktion_grundpreis=aktion_grundpreis, category=category,
            aktion=aktion)
    return c

def populate():
    supermarket = Supermarket.objects.get(pk=1)
    for item in main():
        if item:
            i_name = item[0]
            menge = item[1]
            Item.objects.create(supermarket=supermarket, i_name=i_name, menge=menge)
            #inhalt = item[2]
            #aktion_price = item[3]
            #normal_price = item[4]
            #aktion_grundpreis = item[5]
            #aktion = item[6]
            #category = 'placeholder'
            #add_items(supermarket, i_name, menge, inhalt, aktion_price, normal_price, aktion_grundpreis, category, aktion) 
if __name__ == '__main__':
#    settings.configure()
#    django.setup()
#    from supermarkets.models import Supermarket, Item
#
#    populate()
    with open('supermarkets/fixtures/first_dump.json', 'w') as file:
        items = main()
        file.write(json.JSONEncoder.encode({items}))
