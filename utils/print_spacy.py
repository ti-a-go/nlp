def print_spacy(spacy):
    print(spacy)
    print(f"tipo da variável spacy: {type(spacy)}")
    print(dir(spacy))
    print(f"tipo da variável spacy.load: {type(spacy.load)}")
    print(spacy)

    pipeline_pt = spacy.load("pt_core_news_lg")
    print("tipo da variável nlp")
    print(type(pipeline_pt))
    print(pipeline_pt)

    print(pipeline_pt("Receba esse shalon"))