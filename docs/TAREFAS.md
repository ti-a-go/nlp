# DESCRIÇÃO DAS TAREFAS

## 1. Comparar os modelos linguísticos utilizados pelas diferentes bibliotecas de NLP
---

    Porquê que vale a pena fazer essa comparação?

### 1.1 Comparar os Tokenizadores
---
Escolhi começar a comparação pelo tokenizador porque ele é o primeiro modelo que processa o corpus e com base na tokenização feita por ele é que os outros modelos vão poder adicionar anotações.

#### Como fazer a comparação?

* Juntar um corpus
* Tokenizar o corpus utilizando vários tokenizadores direfentes
* **Desenvolver uma metodologia de comparação**
* Comparar
* Analizar os resultados da comparação


#### Metodologia de comparação

Depois de tokenizar o corpus, é preciso gerar metadados sobre a tokenização.

Ex:
* quantidade de token gerados
* quantidade de token **identicos** entre os diferentes tokenizadores
* quantidade de token **diferentes** entre os diferentes tokenizadores
    * Essa é uma boa medida para classificar a eficiência do tokenizador? 
* Quantos token incorretamente gerados por cada tokenizador
    * Essa é uma boa medida para classificar a efiniência do tokenizador?

#### Engenharia

Como vai ser a solução técinica?

É necessário uma interface (RESTFull API possivelmente) que vai receber o dado bruto (txt) para ser tokenizado.