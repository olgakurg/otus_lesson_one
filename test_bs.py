import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_links(url):        
    
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    hrefs = set()

    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None or 'http' not in href or urlparse(url).hostname == urlparse(href).hostname:
            continue
        hrefs.add(href)

    if param1 == 'c':
        print (f'\nДля ссылки {url} получили набор ссылок:')
        for link in hrefs:
            print(f'{link}')
    elif param1 == 'f':
        with open(path, 'a', encoding='utf-8') as file:
            file.write(f'\nДля ссылки {url} получили набор ссылок:')
            for link in hrefs:
                file.write(f'{link} \n')
        
    return hrefs


  

if __name__ == '__main__':
       
    url = 'http://edu.buk.irk.ru'
    path = 'test.txt'

    print (f'Парсим {url}')
    param1 = input(f'Сохраняем результаты в файл {path} (f) или выводим в терминал (с)? ')
    param2 = input (f'Для каждой полученной ссылки процедуру повторяем (у/n)? ')

    if param1 and param2:
        urls = get_links(url)
        if param2 == 'y':
            for url in urls:
                new_urls = get_links(url)
    else:
        print ('неизвестные параметры, проверьте раскладку и запустите заново')