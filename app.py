#!/usr/bin/python
# -*- coding: utf-8 -*-
from funcs.funcs import monta_indice_arquivo, calcula_distancia, calcula_classe

BASE_CONHECIMENTO1 = "data/01-train.txt"
ARQUIVOS_TESTE1 = "data/01-test.txt"
BASE_CONHECIMENTO2 = "data/02-train.txt"
ARQUIVOS_TESTE2 = "data/02-test.txt"

QUANT_PARECIDOS = 3
QUANT_CLASSE = 3


def start():
    """
    Funcao main do programa
    """
    print "=== Um Sistema de Recomendação baseado em \
Conteúdo para Sugestão de Notícias Relacionadas ==="

    dic_global = monta_indice_arquivo(BASE_CONHECIMENTO2)
    dic_teste = monta_indice_arquivo(ARQUIVOS_TESTE2)

    for chaves_test in dic_teste:
        list_distancia = []

        print_arquivo_classe(chaves_test, dic_teste[chaves_test][0])

        for chaves_global in dic_global:
            if chaves_test != chaves_global:
                distancia = calcula_distancia(dic_teste[chaves_test], dic_global[chaves_global])
                list_distancia.append([distancia, chaves_global, dic_global[chaves_global][0]])

        list_distancia.sort(key=get_key_sort)

        print_list_distancia(list_distancia, QUANT_PARECIDOS)

        classe_arquivo = calcula_classe(list_distancia)
        classe_arquivo.sort(key=get_key_sort, reverse=True)

        print_list_aleatorio_classe(list_distancia, classe_arquivo[0][1], QUANT_CLASSE)

        print


def get_key_sort(l):
    """
    Funcao auxiliar para o metodo sorted dos lists.
    Como a lista que sera ordenada tem o formato:
    [[A, B], [C, D], [E, F], [G, H]]
    Eh necessario um metodo que retorne qual valor das listas internas sera usado para ordenar

    :param l: lista com o formato desejado para ordenacao
    :return: retorna a sublista
    """
    return l[0]


def print_arquivo_classe(path, classe):
    """
    Printa qual arquiro sera usado como entrada no momento
    :param path: o arquivo (caminho) que sera usado
    :param classe: classe do arquivo que esta sendo usado
    """
    print
    print path, classe


def print_list_distancia(list_distancia, quant_loops):
    """
    Printa uma lista contendo o arquivo que foi feito o calculo e a distancia em si
    :param list_distancia: lista de arquivos que foram calculados
    :param quant_loops: quantidade de arquivos que serao impressos no terminal
    """
    print '--------------------------'
    print 'Textos mais parecidos'
    print '--------------------------'

    k = 0

    while k < quant_loops and k < len(list_distancia):
        print list_distancia[k][1], list_distancia[k][0]
        k += 1


def print_list_aleatorio_classe(list_distancia, classe, quant_loops):
    print '--------------------------'
    print 'Textos texto aleatorios da mesma classe (' + classe + ")"
    print '--------------------------'

    k = 0
    while k < quant_loops and k < len(list_distancia):
        if list_distancia[k][2] == classe:
            print list_distancia[k][1]
        k += 1

if __name__ == "__main__":
    start()