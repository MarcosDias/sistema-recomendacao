#!/usr/bin/python
# -*- coding: utf-8 -*-
from funcs.funcs import monta_indice_arquivo, calcula_distancia

BASE_CONHECIMENTO1 = "data/01-train.txt"
ARQUIVOS_TESTE1 = "data/01-test.txt"
BASE_CONHECIMENTO2 = "data/02-train.txt"
ARQUIVOS_TESTE2 = "data/02-test.txt"


def start():
    """
    Funcao main do programa
    """
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
    k = 0
    print '--------------------------'
    print 'Textos mais parecidos'
    print '--------------------------'
    while k < quant_loops and k < len(list_distancia):
        print list_distancia[k][1], list_distancia[k][0]
        k += 1

if __name__ == "__main__":
    start()