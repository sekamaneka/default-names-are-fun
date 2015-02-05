import requests
from collections import Counter
import re

items=list()
def finding_matching_table():
    r = requests.get('https://www.billa.at/Flugblatt/Angebotsliste/Angebote_Aktion/dd_bi_channelpage.aspx')
    saved = False
    table = list()
    for line in r.text.split('\n'):
        if ('summary') in line:
            saved=True
            table.append(line)
        if saved:
            table.append(line)
        if '</table>' in line:
            break
    return table

def finding_items_in_the_table(table):
    saved = False
    items = list()
    for line in table:
        if '<tr>' in line:
            saved=True
            kat = ''
        if '</tr>' in line:
            saved = False
            items.append(kat)
        if '<abbr' in line:
            continue
        if saved:
            kat += line 
    return items

def dividing_into_list(items):
    prog = re.compile(r'<td.*?>(?P<info>.*?)</td>')
    list_of_lists = list(list())
    for i in items:
        menge = prog.findall(i) 
        for i in range(7-len(menge)):
            menge.append('')
        list_of_lists.append(menge)


    return list_of_lists

def main():
    items = finding_items_in_the_table(finding_matching_table())
    i = (dividing_into_list(items))
    return i
