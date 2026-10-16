import random

from astar import astar
from mapa import CUSTOS

TERRENOS = ['.', '~', '*', '#', 'J']
PESOS = [60, 15, 10, 12, 3]


def sortear_terreno():
    return random.choices(TERRENOS, weights=PESOS)[0]


def gerar_mapa(linhas=10, colunas=15, seed=None):
    if seed is not None:
        random.seed(seed)

    inicio = (0, 0)
    fim = (linhas - 1, colunas - 1)

    while True:
        mapa = []
        for l in range(linhas):
            linha = ''
            for c in range(colunas):
                if (l, c) == inicio:
                    linha += 'S'
                elif (l, c) == fim:
                    linha += 'G'
                else:
                    linha += sortear_terreno()
            mapa.append(linha)

        custo, caminho = astar(inicio, fim, mapa, CUSTOS)
        if custo is not None:
            return mapa