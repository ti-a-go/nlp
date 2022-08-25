"""
significado das tags:
https://universaldependencies.org/u/pos/
https://stackoverflow.com/questions/40288323/what-do-spacys-part-of-speech-and-dependency-tags-mean
"""
import spacy

nlp = spacy.load('pt_core_news_lg')
text = "Nos anos 50, João Cândido é encontrado esquecido pela história, vendendo peixe na beira da mesma Baía de Guanabara que fez dele um herói. Mas o que exatamente ele fez para merecer isso?"
doc = nlp(text)
for token in doc:
    print(f'token: {token}')
    print(f'pos: {token.pos_}')
    print(f'morth: {token.morph}')
    print(f'dep: {token.dep_}')
    print('=================')
