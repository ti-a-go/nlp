from wiki import Wiki

def test_wiki_search():
    wiki = Wiki()
    results = wiki.search()
    print(results)
