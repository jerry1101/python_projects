import requests
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import multiprocessing
#import re


def prepare_complete_links(url):

    #http_regex = re.compile(r'http')
    page = requests.get(url)
    http_encoding = page.encoding if 'charset' in page.headers.get('content-type', '').lower() else None
    html_encoding = EncodingDetector.find_declared_encoding(page.content, is_html=True)
    encoding = html_encoding or http_encoding
    soup = BeautifulSoup(page.content, 'html.parser', from_encoding=encoding)
    complete_links = []
    for link in soup.find_all('loc'):
        complete_links.append(link.text)
        print( link.text)

    return list(set(complete_links))


def log_response(message, history_file='./response.txt'):
    history = open(history_file, "a+")
    history.write(message)
    history.write("\n")


def collect_http_status_code(sitemap_url_list):
    index = 0
    for link in sitemap_url_list:
        index += 1
        res = requests.get(link)
        if res.status_code > 200:
            print(link + ' status_code is ', res.status_code)
            log_response(link + ' status_code is ', res.status_code)
        print(":", index, 'status_code is ', res.status_code)


def new_collect_http_status_code(url):
    try:
        res = requests.get(url)
        if res.status_code > 200:
            print('--> '+url + ' status_code is ', res.status_code)
            log_response(url + ' status_code is '+ res.status_code)
        print(url + ' status_code is ', res.status_code)
    except Exception:
        log_response(url, history_file='./error.txt')


def main():
    sitemap_url_list = prepare_complete_links('http://www.totalwine.com/Product-en-USD-2-3105638302377772234.xml')
    print('number of links: ', len(sitemap_url_list))
    print('Start fetching http status')
    pool = multiprocessing.Pool(processes=6)
    print(pool.map(new_collect_http_status_code, sitemap_url_list))
    print('End')


if __name__ == '__main__':

    main()


