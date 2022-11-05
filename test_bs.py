import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def is_not_external(href, url):
    if urlparse(url).hostname == urlparse(href).hostname:
        return True
    else:
        return False

def get_links(url):        
    
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    hrefs = set()

    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None or '//' not in href or is_not_external(href, url):
            continue
        hrefs.add(href)
        
    return hrefs

if __name__ == '__main__':
       
    url = 'http://edu.buk.irk.ru'
    urls = get_links(url)
    for url in urls:
        new_urls = get_links(url)
        print (new_urls)


    #TODO  - регулярка для внутренних ссылок, доделать джампы. потом - вывод в файл или в консоль