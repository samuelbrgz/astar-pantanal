from mapa import movimentos, manhattan
import heapq

def reconstruir_caminho(veio_de, atual):
    caminho = [atual]
    while atual in veio_de:
        atual = veio_de[atual]
        caminho.append(atual)
    caminho.reverse()
    return caminho

def astar(inicio, fim, MAPA, CUSTOS):
    fila = []
    heapq.heappush(fila, (manhattan(inicio, fim), inicio))
    g = {inicio: 0}
    veio_de = {}

    while fila:
        f, atual = heapq.heappop(fila)
        if atual == fim:
            return g[fim], reconstruir_caminho(veio_de, fim)

        for vizinho, custo in movimentos(atual, MAPA, CUSTOS):
            novo_g = g[atual] + custo
            if vizinho not in g or novo_g < g[vizinho]:
                g[vizinho] = novo_g
                veio_de[vizinho] = atual
                heapq.heappush(fila, (novo_g + manhattan(vizinho, fim), vizinho))

    return None, None  # sem caminho