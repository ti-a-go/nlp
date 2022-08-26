from typing import List
import requests

from bs4 import BeautifulSoup
import wikipedia #https://wikipedia.readthedocs.io/en/latest/code.html

from utils.logger import get_logger

log = get_logger('scrapper')

def scrap_wikipedia():
    log = get_logger('scrapper')
    url = 'https://pt.wikipedia.org/wiki/Categoria:Hist%C3%B3ria_dos_afro-brasileiros'
    res = requests.get(url)
    page = res.content.decode('utf-8')
    # log.info(page)
    # log.info(type(page))
    soup = BeautifulSoup(page, 'html.parser')
    # log.info(soup)
    # log.info(type(soup))
    element = soup.find_all('div', {'class': 'CategoryTreeItem'})
    # log.info(len(element))
    # log.info(type(element))
    links = soup.find_all('a')
    # log.info(links)
    # log.info(len(links))
    return None

class Wiki:

    def __init__(self) -> None:
        self.w = wikipedia

    def search(self, query) -> List[str]:
        self.results = dict()
        self.results[query] = self.w.search(query)
        return self.results
    

def wiki():
    # query = 'História dos afro-brasileiros'
    # results = wikipedia.search(query)
    # # log.info(result)
    # # log.info(type(result))
    # suggestions = wikipedia.suggest('brasil')
    # log.info(type(suggestions))
    # log.info(suggestions)
    # summary = wikipedia.summary(query)
    # log.info(type(summary))
    # log.info(summary)
    # page = wikipedia.page(result[0])
    # log.info(type(page))
    # log.info(page)
    # for result in results:
    #     page = wikipedia.page(result)
    #     print(page)

    
