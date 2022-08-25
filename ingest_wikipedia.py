from argparse import ArgumentParser
import mwclient

from utils.logger import get_logger


log = get_logger('ingest_wikipedia')

def ingest_wikipedia(query: str, lang: str = 'pt'):
    site = mwclient.Site(f'{lang}.wikipedia.org')
    page = site.pages[query]
    with open(f'datalake/wikipedia/{query}.txt', 'w', encoding='utf-8') as file:
        file.write(page.text())

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('query', nargs=1,
                        help='what to search in wikipedia')
    args = vars(parser.parse_args())
    query = args['query'][0]
    log.info(f'Ingesting {query} from Wikipedia')
    ingest_wikipedia(query)