import os
from wordcloud import WordCloud
import spacy


# inputs:
# txt_file, words_file, image_file
txt_file = 'datalake/machado_de_assis/romance/MemoriasBras.txt'
words_file = 'data_warehouse/wordcloud/machado_de_assis/memoriasBras.txt'
image_file = 'data_warehouse/wordcloud/machado_de_assis/memoriasBras.png'


with open(os.path.join(txt_file), 'r') as f:
    text = f.read()
# Carrega o modelo da língua portuguesa
nlp = spacy.load('pt_core_news_lg')
# Processa os dados e cria um Doc
doc = nlp(text)
# cria a lista de palavras
words = ''
for token in doc:
    if token.pos_ == 'PROPN':
        if token.text != 'SE':
            words += token.text_with_ws
# cria a wordcloud
wordcloud = WordCloud(width=2000, height=1000).generate(words)
# salva a wordcloud no formato image
with open(words_file, 'r') as f:
    image = wordcloud.to_image()
    image.save(os.path.join(image_file))
    