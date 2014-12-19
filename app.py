#!/usr/bin/python
# -*- coding: utf-8 -*-
from funcs.funcs import monta_indice_arquivo, calcula_distancia

BASE_CONHECIMENTO1 = "data/01-train.txt"
ARQUIVOS_TESTE1 = "data/01-test.txt"
BASE_CONHECIMENTO2 = "data/02-train.txt"
ARQUIVOS_TESTE2 = "data/02-test.txt"


def start():
    print "=== Um Sistema de Recomendação baseado em \
Conteúdo para Sugestão de Notícias Relacionadas ==="

    dic_global = monta_indice_arquivo(BASE_CONHECIMENTO1)
    dic_teste = monta_indice_arquivo(ARQUIVOS_TESTE1)

    for chaves_test in dic_teste:
        list_distancia = []

        print_arquivo_classe(chaves_test, dic_teste[chaves_test][0])

        for chaves_global in dic_global:
            if chaves_test != chaves_global:
                distancia = calcula_distancia(dic_teste[chaves_test], dic_global[chaves_global])
                list_distancia.append([distancia, chaves_global])

        list_distancia.sort(key=get_key_sort)

        print_list_distancia(list_distancia, 3)


def get_key_sort(l):
    return l[0]


def print_arquivo_classe(path, classe):
    print
    print path, classe


def print_list_distancia(list_distancia, quant_loops):
    k = 0
    print '--------------------------'
    print 'Textos mais parecidos'
    print '--------------------------'
    while k < quant_loops and k < len(list_distancia):
        print list_distancia[k][1], list_distancia[k][0]
        k += 1

if __name__ == "__main__":
    start()