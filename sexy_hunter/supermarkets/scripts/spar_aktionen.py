import requests
import re

plus = requests.get(
    'http://www.spar.at/de_AT/index/aktionen/1-1-gratis-aktionen.html')
sparangebote = requests.get(
    'http://www.spar.at/de_AT/index/aktionen/SPARAngebote.html')

def main():
    find_links_for_monatsparer_produkts(monatssparer)
    find_links_for_monatsparer_produkts(plus)
    find_links_for_monatsparer_produkts(sparangebote)
def find_links_for_monatsparer_produkts():
    links_reg = re.compile(r'value="(?P<link>.*html)')
    img_reg = re.compile(r'value="(?P<img>.*jpg)')
    name = re.compile(r'value="(?P<name>.*)" ')
    monatssparer = requests.get(
        'http://www.spar.at/de_AT/index/aktionen/Monatssparer.html')
    imgs = list()
    links = list()
    names = list()
    for line in monatssparer.text.split('\n'):
        if 'class="socialMediaImage' in line:
            found_imgs = img_reg.findall(line)
            imgs.append(str(found_imgs))
        elif 'class="socialMediaLink' in line:
            found_links = links_reg.findall(line)
            links.append(str(found_links))
        #elif 'class="socialMediaImage' in line:
        elif 'class="socialMediaTitle' in line:
            found_name = name.findall(line)
            names.append(str(found_name))
    return zip(imgs, links, names)

