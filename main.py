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


def load_raw_text(file_path) -> str:
    text = ""
    try:
        with open(file_path, encoding='utf-8') as f:
            text = text + f.read()
    except OSError as err:
        print(f'An OSError occurred when trying to open the file: {err}')
    except Exception as exc:
        print(f'An unpexted error occurred when trying to open the file: {exc}')

    return text


def main():
    text_name = 'historiasSemData'
    genero = 'conto'
    file_path = f"datalake/machado_de_assis/{genero}/{text_name}.txt"
    raw_data = load_raw_text(file_path)
    lang = "pt"
    doc = convert_str_to_doc(raw_data, lang)
    df = convert_doc_to_df(doc)
    csv_file_name = f"{text_name}.csv"
    df.to_csv(csv_file_name)


if __name__ == '__main__':
    main()
