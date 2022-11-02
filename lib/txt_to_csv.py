import spacy
import pandas as pd
from spacy.tokens.doc import Doc
from argparse import ArgumentParser


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


def doc_to_df(doc: Doc) -> pd.DataFrame:
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


def txt_to_csv(input_file_path: str, output_file_path: str, lang: str):
    df = doc_to_df(convert_str_to_doc(load_raw_text(input_file_path), lang))
    return df.to_csv(output_file_path)


if __name__ == '__main__':
    # args: input_file_path, where to read the txt file.
    # args: output_file_path, where to write the generated csv file. 
    # args: lang, ['pt', 'en', 'es', 'fr', 'de', 'it']
    parser = ArgumentParser()
    parser.add_argument('-p', '--path', dest='input_file_path', required=True,
                        help='where to read the txt file.')
    parser.add_argument('-o', '--output', dest='output_file_path', required=True,
                        help='where to write the generated csv file.')
    parser.add_argument('-lang', dest='lang', default='pt',
                        help='["pt", "en", "es", "fr", "de", "it"]',
                        required=False, choices=['pt', 'en', 'es', 'fr', 'de', 'it'])

    args = parser.parse_args()
    print(vars(args))
