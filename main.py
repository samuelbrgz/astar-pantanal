from gerador import gerar_mapa
from benchmark import executar, benchmark, imprimir_tabela, grafico_comparacao
from visual import desenhar_comparacao


def main():
    # 1) Um mapa só, com o caminho de cada algoritmo lado a lado
    mapa = gerar_mapa(linhas=10, colunas=10, seed=29    )
    print('Mapa gerado:')
    for linha in mapa:
        print(linha)

    resultados = executar(mapa)
    for nome, r in resultados.items():
        print(f"{nome}: custo={r['custo']}, nós expandidos={r['expandidos']}, "
              f"tempo={r['tempo']:.3f} ms")
    desenhar_comparacao(mapa, resultados)

    # 2) Estatísticas em vários mapas aleatórios
    dados = benchmark(n_mapas=30, linhas=10, colunas=10)
    imprimir_tabela(dados)
    grafico_comparacao(dados)


if __name__ == '__main__':
    main()