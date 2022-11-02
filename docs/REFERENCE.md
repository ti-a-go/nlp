# main.py

[código](../main.py)
```py
from utils.txt_to_csv import txt_to_csv


text_name = 'variasHistorias'
genero = 'conto'
dataset_name = 'machado_de_assis'
file_path = f"datalake/{dataset_name}/{genero}/{text_name}.txt"
lang = "pt"
csv_file_name = f"data_warehouse/{dataset_name}/{genero}/{text_name}.csv"
txt_to_csv(file_path, csv_file_name, lang)
```


# txt_to_csv()
[código](../lib/txt_to_csv.py)
``` py
txt_to_csv(input_file_path: str, output_file_path: str, lang: str)
```

Cria um arquivo csv com as anotações feitas por um dos modelos da biblioteca Spacy

## Modelos suportados
* pt_core_news_lg
* en_core_web_trf
* es_dep_news_trf
* fr_dep_news_trf
* de_dep_news_trf
* it_core_news_lg
