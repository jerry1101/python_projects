import requests
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import re


TWM_DOMAIN = "http://www.totalwine.com"


def prepare_complete_links(url):

    http_regex = re.compile(r'http')
    page = requests.get(url)
    http_encoding = page.encoding if 'charset' in page.headers.get('content-type', '').lower() else None
    html_encoding = EncodingDetector.find_declared_encoding(page.content, is_html=True)
    encoding = html_encoding or http_encoding
    soup = BeautifulSoup(page.content, 'html.parser', from_encoding=encoding)
    complete_links = []
    for alink in soup.find_all('a', href=True):
        if http_regex.search(alink['href']) is not None:
            complete_links.append(alink['href'])
            print(http_regex.search(alink['href']).group()+"---"+alink['href'])
        elif 'javascript' not in alink['href'] and len(alink['href'].strip()) > 0:
            if alink['href'][:1] == '/':
                temp_link = TWM_DOMAIN + alink['href']
                complete_links.append(temp_link)
                print("need http" + "---" + alink['href'])
            else:
                temp_link = TWM_DOMAIN+"/" + alink['href']
                complete_links.append(temp_link)

    return list(set(complete_links))


####################

list_links = prepare_complete_links('http://www.totalwine.com/sitemap')


for link in list_links:
    res = requests.get(link)
    if res.status_code > 200:
        print(link+' status_code is ', res.status_code)



