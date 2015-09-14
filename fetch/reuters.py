"""Scrape routers pages"""

import requests
import re
import os
import pprint
import json
from urllib.parse import urlparse
from urllib.parse import urljoin
from bs4 import BeautifulSoup

pp = pprint.PrettyPrinter(indent=2)
links = set()
visited_links = set()
article_links = set()
dataset = {}

article_link_regex = r'reuters.com/article'
start_url = "http://www.reuters.com"

def is_article(url):
    return re.search(article_link_regex, str(url)) != None

def with_base_url(baseUrl, hrefs):
    return [urljoin(baseUrl, x) for x in hrefs if re.search(r'^/', str(x)) != None]

def get_html_node(soup, name, attrs, value_attr):
    node = soup.find(name, attrs=attrs)
    if node != None:
        return node.get(value_attr)
    else:
        return None

def get_page(url):
    print('getting', url)
    url_structure = urlparse(url)
    visited_links.add(url)
    soup = BeautifulSoup(requests.get(url).text, 'html5lib')
    local_links = with_base_url(url, (a.get('href') for a in soup('a')))
    local_article_links = [x for x in local_links if re.search(article_link_regex, str(x)) != None]

    if is_article(url):
        canonical = get_html_node(soup, 'link', {'rel':'canonical'}, 'href')
        fn_title = get_html_node(soup, 'meta', {'property':'og:title'}, 'content')
        keywords = get_html_node(soup, 'meta', {'name':'keywords'}, 'content')
        author = get_html_node(soup, 'meta', {'name':'Author'}, 'content')

        if canonical:
            visited_links.add(canonical)

        dataset[url] = {
            'fb_title': fn_title,
            'canonical': canonical or url,
            'keywords': keywords,
            'author': author,
            'local_links': local_links,
            'local_article_links': local_article_links
        }

    links.update(local_links)
    article_links.update(local_article_links)
    print(len(links.difference(visited_links)), 'links left')

get_page(start_url)

while len(links.difference(visited_links)) and len(visited_links) < 10:
    for link in set(links).difference(visited_links):
        get_page(link)


print('\nall links:\n')
pp.pprint(links) #needs to be db
print('\nvisited links:\n')
pp.pprint(visited_links) #needs to be db
print('\nfound articles:\n')
pp.pprint(article_links)
print('\nfound dataset:\n')
pp.pprint(dataset)
