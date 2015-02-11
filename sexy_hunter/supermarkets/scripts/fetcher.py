# have to return standard values with all scripts
# name, link, url

import requests
import re


def finding_matching_table():
    ''' this returns the html table holding all elements in the page below
    '''

    r = requests.get('https://www.billa.at/Flugblatt'
                     '/Angebotsliste/Angebote_Aktion/dd_bi_channelpage.aspx')
    saved = False
    table = list()
    for line in r.text.split('\n'):
        if ('summary') in line:
            saved = True
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
            saved = True
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
    prog = re.compile(r'<td>(?P<info>.*?)</td>')
    head = re.compile(r'<td.*?>(?P<info>.*?)</td>')
    list_of_lists = list(list())
    for i in items:
        menge = prog.findall(i)
        ha = head.search(i)
        if ha:
            menge.append(ha.group(1).replace('<br>', '').replace('</br>', ''))
        list_of_lists.append(
            [j.replace('nbsp', '').replace('&', '').replace(';', ' ').
             replace('<br>', '\n').replace('statt', '').
             replace('Region', '.\nRegion') for j in menge])
    return list_of_lists


def main():
    items = finding_items_in_the_table(finding_matching_table())
    i = (dividing_into_list(items))
    return i
main()
