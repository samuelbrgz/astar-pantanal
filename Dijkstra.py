import heapq


from astar import reconstruir_caminho

matriz = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

def Dijkstra(inicio,fim, matriz, custo):
    linhas = len(matriz)
    colunas = len(matriz[0])

    nova_matriz = [[0]* colunas for _ in range(linhas)]
    for linha in range(linhas):
        for coluna in range(colunas):
             nova_matriz[linha][coluna] = custo.get(matriz[linha][coluna], float('inf'))


    distancias = [[float('inf')] * colunas for _ in range(linhas)]
    #aqui to iniciando com infinito, esse float("inf") * coluna cria uma linha com essa quantidade de colunas, nesse caso tudo com inf. e o for _ in vai percorrer tods as linhas da matriz

    linha_origem, coluna_origem = inicio

    distancias[linha_origem][coluna_origem] = nova_matriz[linha_origem][coluna_origem]

    fila = [(nova_matriz[linha_origem][coluna_origem], linha_origem, coluna_origem)]

    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    veio_de = {}

    while fila:
        distancia_atual, l, c = heapq.heappop(fila)


        if(l,c) == fim:
            return distancia_atual, reconstruir_caminho(veio_de, fim)

        if distancia_atual > distancias[l][c]:
            continue

        for deslocamento_linha, deslocamento_coluna in movimentos:
            nova_linha, nova_coluna = l+deslocamento_linha, c+deslocamento_coluna
            if 0<= nova_linha < linhas and 0 <= nova_coluna< colunas:
                novo_custo = distancia_atual + nova_matriz[nova_linha][nova_coluna]

                if novo_custo < distancias[nova_linha][nova_coluna]:
                    distancias[nova_linha][nova_coluna] = novo_custo
                    veio_de[(nova_linha, nova_coluna)] = (l, c)
                    heapq.heappush(fila, (novo_custo, nova_linha, nova_coluna))
    return -1







