import spacy
import pandas as pd
from spacy.tokens.doc import Doc
from pandas import DataFrame


def convert_str_to_doc(text: str, lang: str) -> Doc:
    lang_available = {
        "pt": "pt_core_news_lg",
        "en": "en_core_web_trf",
        "es": "es_dep_news_trf",
        "fr": "fr_dep_news_trf",
        "de": "de_dep_news_trf",
        "it": "it_core_news_lg",
    }

    pipeline = spacy.load(lang_available[lang])

    return pipeline(text)


def convert_doc_to_df(doc: Doc) -> DataFrame:
    rows = []
    columns = ["text", "lemma", "pos", "tag", "morph",
               "ent_type", "is_punct", "dep", "sentiment"]
    for token in doc:
        rows.append([token.text, token.lemma_, token.pos_, token.tag_,
                     token.morph, token.ent_type_, token.is_punct,
                     token.dep_, token.sentiment])

    return pd.DataFrame(rows, columns=columns)


def load_raw_text(file_path):
    text = ""
    with open(file_path) as f:
        text = text + f.read()

    return text


def main():
    lang = "pt"
    text_name = 'historiasMeiaNoite'
    genero = 'conto'
    file_path = f"datalake/machado_de_assis/{genero}/{text_name}.txt"
    csv_file_name = f"{text_name}.csv"
    doc = convert_str_to_doc(load_raw_text(file_path), lang)
    df = convert_doc_to_df(doc)
    df.to_csv(csv_file_name)


if __name__ == '__main__':
    main()
