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
    base = []
    with open(path) as f:
        data = f.read().splitlines()
        for arquivo in data:
            base.append(arquivo.split(' '))

        return base


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
    base = monta_arquivos(path_arquivo)
    for arq in base:
        dic[arq[0]] = [arq[1], monta_indice(arq[0])]

    return dic


def calcula_distancia(list_test, list_global):
    """
    Recebe os valores dos dicionarios de indice globla e o de test,
    esses valores tem um formato de uma lista
    como segue o exemplo:
    ['sports', {'bola': 4, 'gol': 2, 'neymar': 1}]
    E calcula a distancia (euclidiana) entre os indices

    :param list_test: lista contendo a classe e o dicionario de indices do test
    :param list_global: lista contendo a classe e o dicionario de indices da base de conhecimento (global)
    :return: retorna a distancia calculada
    """
    words_test = list_test[1]
    words_global = list_global[1]
    distancia = 0

    for chave in words_test:
        if chave in words_global:
            distancia += (words_test[chave] - words_global[chave]) ** 2
        else:
            distancia += (words_test[chave]) ** 2

    for chave in words_global:
        if chave not in words_test:
            distancia += (words_global[chave]) ** 2

    return distancia


def get_maior_distancia(list_distancia):
    """
    Calcula a maior distancia dentro da lista
    A lista tem esse formato:
    [[DISTANCIA, ARQUIVO, CLASSE]]

    :param list_distancia: lista contendo as distancias entre os arquivos
    :return: retorna a maior distancia entre as distancias dos arquivos
    """
    maior = 0
    for corpo in list_distancia:
        if corpo[0] > maior:
            maior = corpo[0]
    return maior


def existe_em(lista, classe):
    """
    Funcao auxiliar que verifica se existe a classe na lista.
    Essa funcao ajudarah na filtragem das classes que ja foram contadas

    :param lista: Lista de apoio para calcular qual a classe do arquivo
    :param classe: Classe que estamos pesquisando
    :return: retorna True, se for encontrado, e False caso contrario
    """
    if len(lista) > 0:
        for corpo in lista:
            if classe in corpo:
                return True

    return False


def soma_distancias(classe, list_distancia, maior_distancia):
    """
    Dado classe de um arquivo e a lista das distancias de formato:
    [[DISTANCIA, ARQUIVO, CLASSE]]
    soma todas as distancias de uma classe

    :param classe: Classe que sera contada
    :param list_distancia: lista contendo as distancias dos arquivos
    :param maior_distancia: maior distancia entre todas
    :return: retorna a soma das distancias de uma classe especifica
    """
    soma = 0
    for corpo in list_distancia:
        if corpo[2] == classe:
            soma += (maior_distancia * 1.0) / corpo[0]

    return soma


# [[DISTANCIA, ARQUIVO, CLASSE]]
def calcula_classe(list_distancia):
    classe_distancia = []

    for corpo in list_distancia:
        if not existe_em(classe_distancia, corpo[2]):
            soma_classe = soma_distancias(corpo[2], list_distancia, get_maior_distancia(list_distancia))
            classe_distancia.append([soma_classe, corpo[2]])

    return classe_distancia


if __name__ == "__main__":
    BASE_CONHECIMENTO1 = "../data/01-train.txt"
    ARQUIVOS_TESTE1 = "../data/01-test.txt"

    print monta_indice_arquivo(BASE_CONHECIMENTO1)