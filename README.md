# Descrição

O objetivo é aplicar técnicas de Processamento de Linguagem Natural para extrair valor de dados textuais.

---

# Plataforma de dados

Para dar facilitar a aplicação dessas tecnicas é necessário uma plataforma de dados com foco em dados textuais não extruturados.

Existem diversas ferramentas em python que podem ajudar nesse trabalho e essa plataforma vai tirar proveito dessas ferramentas open source.

## Serviços

Inicialmente essa plataforma será um conjunto de serviços.

### ETL

Um dos serviços que serão uteis desde o início é o de extração, transformação e carregamento de dados textuais. Esse serviço tem grandes chances de ser um dos primeiros a serem desenvolvidos.

### Armazenamento de dados

Outro serviço importante é o armazenamento dos dados a serem analisados.

### Ferramentas de Análise

Esse é um dos principais serviços da plataforma já que é utilizado na Analise de Dados que é o carro chefe desse projeto.

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

---

# Como organizar os dados

Para facilitar o processamento é necessário que os dados estejam em formato texto (.txt) para poderem ser processados pelas ferramentas que utilizaremos na plataforma.

Além dos textos, é preciso ter metadados sobre esses textos que podem estar em formatos de tabela (.csv preferencialmente).

## A estrutura de pastas

Inicialmente os dados serão armazenados junto com o código do projeto. Para fins de organização será definida uma estrutura de pastas para armazenar os dados e seus metadados.

Dentro da pasta data/ existe várias outras pastas que correspondem a um conjunto: texto.txt metadata.csv.


---

# Webserver

