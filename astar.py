from mapa import movimentos, inifim, manhattan, MAPA, CUSTOS
import heapq

def astar(inicio, fim, MAPA, CUSTOS):
    fila = []
    heapq.heappush(fila, (manhattan(inicio, fim), inicio))
    g = {
       inicio: 0, 
    }
    veio_de = {}

    while fila:
       f, atual = heapq.heappop(fila)
       if atual == fim:
           return g[fim]
       else:
            for vizinho, custo in movimentos(atual, MAPA, CUSTOS):
              novo_g = g[atual] + custo
            if vizinho not in g or novo_g < g[vizinho]:
               g[vizinho] = novo_g
               veio_de[vizinho] = atual
               heapq.heappush(fila, (novo_g + manhattan(vizinho, fim), vizinho))
