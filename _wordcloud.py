import os
from wordcloud import WordCloud
import spacy

file_path = 'datalake/machado_de_assis/romance/MemoriasBras.txt'
with open(os.path.join('datalake/machado_de_assis/romance/MemoriasBras.txt'), 'r') as file_1:
    text = file_1.read()
nlp = spacy.load('pt_core_news_lg')
doc = nlp(text)
with open('data_warehouse/wordcloud/machado_de_assis/memoriasBras.txt', 'w+') as file_2:
    for token in doc:
        if token.pos_ in ['PROPN']:
            if token.text != 'SE':
                file_2.write(f' {token.text} \n')
with open('data_warehouse/wordcloud/machado_de_assis/memoriasBras.txt', 'r') as file:
    wordcloud = WordCloud(width=2000, height=1000).generate(file.read())
    image = wordcloud.to_image()
    image.save(os.path.join('data_warehouse/wordcloud/machado_de_assis/memoriasBras.png'))
    