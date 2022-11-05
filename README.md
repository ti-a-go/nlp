# Descrição

O objetivo é aplicar técnicas de Processamento de Linguagem Natural para extrair valor de dados textuais.

---
# Instalação

Esse projeto utiliza modelos pré-treinados da biblioteca Spacy. Portanto antes de utilizar, baixe os modelos utilizando os seguintes scripts:

``` bash
python -m spacy download pt_core_news_lg
python -m spacy download es_dep_news_trf
python -m spacy download fr_dep_news_trf
python -m spacy download en_core_web_trf
python -m spacy download de_dep_news_trf
python -m spacy download it_core_news_lg
``` 

### Dependencias

Para instalar as dependencias você pode criar um ambiente virtual e instalar os pacotes necessários com o pip

``` bash
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```
