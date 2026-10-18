def Buscaexaustiva(inicio, fim, matriz, custo):
    linhas, colunas = len(matriz), len(matriz[0])

    nova_matriz = [[0]* colunas for _ in range(linhas)]

    for linha in range(linhas):
        for coluna in range(colunas):
            nova_matriz[linha][coluna] = custo.get(matriz[linha][coluna], float('inf'))

    melhor_custo = float('inf')
    melhor_caminho = []

    visitados = set()
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def buscar(l, c, custo_atual, caminho_atual):
        nonlocal melhor_custo, melhor_caminho

        if custo_atual >= melhor_custo:
            return

        if (l, c) == fim:
            melhor_custo = custo_atual
            melhor_caminho = list(caminho_atual)
            return


        visitados.add((l, c))


        for deslocamento_linha, deslocamento_coluna in movimentos:
            nova_linha, nova_coluna = l + deslocamento_linha, c + deslocamento_coluna


            if 0 <= nova_linha < linhas and 0 <= nova_coluna < colunas and (nova_linha, nova_coluna) not in visitados:
                caminho_atual.append((nova_linha, nova_coluna))

                buscar(nova_linha, nova_coluna, custo_atual + nova_matriz[nova_linha][nova_coluna], caminho_atual)


                caminho_atual.pop()


        visitados.remove((l, c))
    origem_l, origem_c = inicio
    custo_inicial = nova_matriz[origem_l][origem_c]

    buscar(origem_l, origem_c, custo_inicial, [inicio])

    if melhor_custo == float('inf'):
        return None, None

    return melhor_custo, melhor_caminho


