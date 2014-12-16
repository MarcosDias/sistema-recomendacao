#!/usr/bin/python
# -*- coding: utf-8 -*-
from funcs.funcs import monta_indice_arquivo


BASE_CONHECIMENTO1 = "../data/01-train.txt"
ARQUIVOS_TESTE1 = "../data/01-test.txt"
BASE_CONHECIMENTO2 = "../data/02-train.txt"
ARQUIVOS_TESTE2 = "../data/02-test.txt"

def start():
    print "Um Sistema de Recomendação baseado em \
    Conteúdo para Sugestão de Notícias Relacionadas"

    dic_global = monta_indice_arquivo(BASE_CONHECIMENTO1)
    dic_teste = monta_indice_arquivo(ARQUIVOS_TESTE1)


