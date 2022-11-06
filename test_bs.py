import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def is_not_external(href, url):
    if 'http' not in href or urlparse(url).hostname == urlparse(href).hostname:
        return True
    else:
        return False

def get_links(url):        
    
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    hrefs = set()

    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None or is_not_external(href, url):
            continue
        hrefs.add(href)
        
    return hrefs

def urls_to_file(url, urls, path):
    with open(path, 'a', encoding='utf-8') as file:
        file.write(f'Для ссылки {url} получили набор ссылок: \n')
        for u in urls:
            file.write(f'link {u} \n')
        


if __name__ == '__main__':
       
    url = 'http://edu.buk.irk.ru'
    path = 'test.txt'

    print (f'Парсим {url}, Вывод результатов в файл {path}')

    urls = get_links(url)
    urls_to_file(url, urls, path)

    for url in urls:
        new_urls = get_links(url)
        urls_to_file(url, new_urls, path)


    #TODO  - доделать джампы. потом - вывод в файл или в консоль