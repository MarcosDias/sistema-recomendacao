#!/usr/bin/python
# -*- coding: utf-8 -*-
import funcs

BASE_CONHECIMENTO1 = "../data/01-train.txt"
ARQUIVOS_TESTE1 = "../data/01-test.txt"
BASE_CONHECIMENTO2 = "../data/02-train.txt"
ARQUIVOS_TESTE2 = "../data/02-test.txt"


def start():
    print "Um Sistema de Recomendação baseado em \
    Conteúdo para Sugestão de Notícias Relacionadas"

    dic_global = funcs.monta_indice_arquivo(BASE_CONHECIMENTO1)
    dic_teste = funcs.monta_indice_arquivo(ARQUIVOS_TESTE1)


if __name__ == "__main__":
    start()


