#!/usr/bin/python
# -*- coding: utf-8 -*-


def monta_arquivos(path):
    """
    Le um arquivo e separa o conteudo onde o primeiro elemento
    eh o caminho do arquivo e o segundo eh a sua classe

    :param path: caminho do arquivo que sera lido
    :return:
        retorna a lista contem a base de dados separada em
        listas onde o primeiro elemento eh o path do
        arquivo e o segundo elemento eh a sua classe
    """
    list = []
    with open(path) as f:
        data = f.read().splitlines()
        for arquivo in data:
            list.append(arquivo.split(' '))

        return list


def monta_indice(path):
    """
    Dado um arquivo, montasse seu indice

    :param path: caminho do arquivo
    :return: retorna um dicionario com o indice das palavras do arquivo
    """
    dic = {}
    with open(path) as f:
        words = f.read()
        for word in words.split(' '):
            if word in dic.keys():
                dic[word] += 1
            else:
                dic[word] = 1

    return dic


def monta_indice_arquivo(path_arquivo):
    """
    Dado o caminho de um arquivo, monta o indice de caminhos contidos no arquivo.
    O dicionario tem esse formato:
    {<path_arquivo1>:[<classe>, {<palavra indexada>:<quantidade de ocorrencias>}];...}

    :param path_arquivo: caminho do arquivo que serah processado
    :return: retorna um dicionario com o indice de cada arquivo escrito no arquivo original
    """
    dic = {}
    list = monta_arquivos(path_arquivo)
    for arq in list:
        dic[arq[0]] = [arq[1], monta_indice(arq[0])]

    return dic


if __name__ == "__main__":
    BASE_CONHECIMENTO1 = "../data/01-train.txt"
    ARQUIVOS_TESTE1 = "../data/01-test.txt"

    print monta_indice_arquivo(BASE_CONHECIMENTO1)