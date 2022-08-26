# from utils.txt_to_csv import txt_to_csv
# from scrapper.main import wiki
from scrapper.wiki import Wiki
from utils.logger import get_logger
from wikipedia import WikipediaPage


log = get_logger('Wiki')

# def convert_text_data_into_tabular_data():
#     text_name = 'variasHistorias'
#     genero = 'conto'
#     dataset_name = 'machado_de_assis'
#     file_path = f"datalake/{dataset_name}/{genero}/{text_name}.txt"
#     lang = "pt"
#     csv_file_name = f"data_warehouse/{dataset_name}/{genero}/{text_name}.csv"
#     txt_to_csv(file_path, csv_file_name, lang)


def main():
    wiki = Wiki()
    queries = ['História dos afro-brasileiros', 'afro-brasileiros']
    query = queries[1]
    # for q in queries:
    #     wiki.search(q)
    # log.info(wiki.results)
    results = wiki.search(query)
    afro_brasileiros_pages_names = results[query]
    afro_brasileiros_pages = list()
    # log.info(afro_brasileiros_pages_names)
    for page_name in afro_brasileiros_pages_names:
        page: WikipediaPage = wiki.w.page(page_name)
        afro_brasileiros_pages.append(page)
        break
    page = afro_brasileiros_pages[0]
    log.info(type(page))
    log.info(type(page.categories))
    log.info(page.categories)

if __name__ == '__main__':
    main()
