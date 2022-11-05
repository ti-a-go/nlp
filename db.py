#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exemplo de CRUD com SQLAlchemy e SQLite3"""

from sqlalchemy import Column, Integer, String, create_engine, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Criar banco na memória
# engine = create_engine('sqlite://')

# Caminho relativo (pode ser utilizado o caminho absoluto):
engine = create_engine('sqlite:///db.sqlite3')

# Para utilizar o debug utilizar deve-se adicionar ``echo=True``:
# engine = create_engine('sqlite:///db.sqlite3', echo=True)

# Criando uma classe "Session" já configurada.
# Session é instanciado posteriormente para interação com a tabela.
Session = sessionmaker(bind=engine)

Base = declarative_base()


class DocMetadata(Base):
    __tablename__ = 'docs_metadata'

    id = Column(Integer, primary_key=True)

    name = Column('name', String(32))
    source = Column('source', String(32))
    url = Column('url', String(32))
    genre = Column('genre', String(20))
    autor = Column('autor', String(32))
    date = Column('date', Date())
    language = Column('language', String(5))

    def __init__(self, nome, idade, sexo):
        """Construtor.

        Utilizando o construtor para passar os valores
        no momento em que a classe é instanciada.

        :param nome: (str).
        :param idade: (int).
        :param sexo: (str).
        """
        self.nome = nome
        self.idade = idade
        self.sexo = sexo


if __name__ == "__main__":
    # Removendo todas as tabelas do banco.
    # Base.metadata.drop_all(engine)

    # Criando todas as tabelas.
    Base.metadata.create_all(engine)

    # Criando uma sessão (add, commit, query, etc).
    session = Session()

    # Criando os dados que serão inseridos na tabela.
    # Classe com o construtor.
    # usuario = NomeDaTabela('Felipe', 35, 'Masculino')
    # usuarios = [NomeDaTabela('Maria', 20, 'Feminino'), NomeDaTabela('Pedro', 50, 'Masculino')]

    # Caso não seja utilizado o construtor na classe
    # os dados são passados depois de se criar a instancia.
    # usuario = NomeDaTabela()
    # usuario.nome = 'Camila'
    # usuario.idade = 50
    # usuario.sexo = 'Feminino'

    # Inserindo registro na tabela.
    # session.add(usuario)

    # Inserindo vários registros na tabela.
    # session.add_all(usuarios)

    # Persistindo os dados.
    # session.commit()

    # Consultar todos os registros.
    # dados = session.query(NomeDaTabela).all()
    # print(dados)
    # for linha in dados:
    #     print(f'Nome: {linha.nome} - Idade: {linha.idade} - Sexo: {linha.sexo}')

    # Consulta registros com filtro.
    # dados = session.query(NomeDaTabela).filter(NomeDaTabela.idade > 40).all()
    # print(dados)
    # for linha in dados:
    #     print(f'Nome: {linha.nome} - Idade: {linha.idade} - Sexo: {linha.sexo}')

    # Alterar um registro da tabela.
    # print('Nome ANTES da alteração:', session.query(NomeDaTabela).filter(NomeDaTabela.id == 1).one().nome)
    # session.query(NomeDaTabela).filter(NomeDaTabela.id == 1).update({'nome': 'Roberto'})
    # session.commit()
    # print('Nome DEPOIS da alteração:', session.query(NomeDaTabela).filter(NomeDaTabela.id == 1).one().nome)

    # Remover um registro da tabela.
    # print('Registro ANTES da remoção:', session.query(NomeDaTabela).filter(NomeDaTabela.id == 1).one_or_none())
    # session.query(NomeDaTabela).filter(NomeDaTabela.id == 1).delete()
    # session.commit()
    # print('Registro DEPOIS da remoção:', session.query(NomeDaTabela).filter(NomeDaTabela.id == 1).one_or_none())

    # Fechando a sessão.
    session.close()
