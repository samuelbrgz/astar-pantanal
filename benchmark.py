import statistics
import time

import matplotlib.pyplot as plt

from gerador import gerar_mapa
from mapa import CUSTOS, inifim
from astar import astar
from Dijkstra import Dijkstra
from BuscaExaustiva import Buscaexaustiva

ALGORITMOS = {
    'A*': astar,
    'Dijkstra': Dijkstra,
    'Exaustiva': Buscaexaustiva,
}

# Quantas vezes cada algoritmo roda por mapa para medir o tempo (fica o menor).
# A exaustiva é lenta, então roda só uma vez.
REPETICOES = {'A*': 5, 'Dijkstra': 5, 'Exaustiva': 1}

CORES = {'A*': '#3d85c6', 'Dijkstra': '#6aa84f', 'Exaustiva': '#e69138'}


def custo_do_caminho(caminho, mapa, custos):
    """Soma o custo das células do caminho, sem contar a célula de início.

    O astar.py não conta o início, mas Dijkstra.py e BuscaExaustiva.py contam.
    Recalcular pelo caminho deixa os três na mesma regra.
    """
    return sum(custos[mapa[l][c]] for l, c in caminho[1:])


def executar(mapa):
    """Roda os 3 algoritmos em um mapa e devolve as métricas de cada um."""
    inicio, fim = inifim(mapa, 'S'), inifim(mapa, 'G')
    resultados = {}
    for nome, func in ALGORITMOS.items():
        tempos = []
        for _ in range(REPETICOES[nome]):
            contador = {'expandidos': 0}
            t0 = time.perf_counter()
            _, caminho = func(inicio, fim, mapa, CUSTOS, contador=contador)
            tempos.append((time.perf_counter() - t0) * 1000)  # ms
        resultados[nome] = {
            'custo': custo_do_caminho(caminho, mapa, CUSTOS),
            'caminho': caminho,
            'expandidos': contador['expandidos'],
            'tempo': min(tempos),
        }
    return resultados


def benchmark(n_mapas=30, linhas=10, colunas=10, seed_base=0):
    """Gera n mapas aleatórios e acumula as métricas de cada algoritmo."""
    dados = {nome: {'custo': [], 'expandidos': [], 'tempo': []}
             for nome in ALGORITMOS}
    for i in range(n_mapas):
        mapa = gerar_mapa(linhas, colunas, seed=seed_base + i)
        resultados = executar(mapa)

        custos = {r['custo'] for r in resultados.values()}
        if len(custos) > 1:
            print(f'Aviso: custos diferentes no mapa {i}: '
                  f'{ {n: r["custo"] for n, r in resultados.items()} }')

        for nome, r in resultados.items():
            for metrica in dados[nome]:
                dados[nome][metrica].append(r[metrica])
    return dados


def media_dp(valores):
    media = statistics.mean(valores)
    dp = statistics.stdev(valores) if len(valores) > 1 else 0.0
    return media, dp


def imprimir_tabela(dados):
    n = len(next(iter(dados.values()))['custo'])
    print(f'\nResultados em {n} mapas aleatórios\n')

    metricas = [('custo', 'Custo'),
                ('expandidos', 'Nós expandidos'),
                ('tempo', 'Tempo (ms)')]

    for chave, rotulo in metricas:
        print(rotulo)
        print(f"{'Algoritmo':<11}{'média':>14}{'dp':>12}"
              f"{'mediana':>14}{'mín':>12}{'máx':>14}")
        for nome, m in dados.items():
            valores = m[chave]
            media, dp = media_dp(valores)
            print(f'{nome:<11}{media:>14,.3f}{dp:>12,.3f}'
                  f'{statistics.median(valores):>14,.3f}'
                  f'{min(valores):>12,.3f}{max(valores):>14,.3f}')
        print()


def grafico_comparacao(dados, salvar=None):
    metricas = [('custo', 'Custo do caminho', False),
                ('expandidos', 'Nós expandidos (escala log)', True),
                ('tempo', 'Tempo em ms (escala log)', True)]
    nomes = list(dados.keys())

    fig, axs = plt.subplots(1, 3, figsize=(14, 5))
    for ax, (chave, titulo, usar_log) in zip(axs, metricas):
        medias = [media_dp(dados[n][chave])[0] for n in nomes]
        desvios = [media_dp(dados[n][chave])[1] for n in nomes]
        # barra de erro de baixo não pode passar de zero (nem da média, no log)
        inferior = [min(d, m * 0.99) for d, m in zip(desvios, medias)]
        ax.bar(nomes, medias, yerr=[inferior, desvios], capsize=6,
               color=[CORES[n] for n in nomes])
        if usar_log:
            ax.set_yscale('log')
        ax.set_title(titulo)
        ax.grid(axis='y', alpha=0.3)
        # a média vai escrita embaixo do nome, para não brigar com a barra de erro
        ax.set_xticks(range(len(nomes)))
        ax.set_xticklabels([f'{n}\n{m:,.1f}' for n, m in zip(nomes, medias)])

    fig.suptitle('A*, Dijkstra e Busca Exaustiva (média ± desvio padrão)')
    fig.tight_layout()
    if salvar:
        fig.savefig(salvar, dpi=150)
    plt.show()