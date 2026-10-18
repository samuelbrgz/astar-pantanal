import sys
from gerador import gerar_mapa
print(sys.executable)

from mapa import CUSTOS, inifim
from astar import astar
from visual import desenhar
from Dijkstra import Dijkstra

def main():
    MAPA = gerar_mapa(linhas=20, colunas=30)
    inicio = inifim(MAPA, 'S')
    fim = inifim(MAPA, 'G')

    custo, caminho = astar(inicio, fim, MAPA, CUSTOS)
    custo_digkstra, caminho_dijkstra = Dijkstra(inicio, fim, MAPA, CUSTOS)
    print('sjkdjhsfjsncjsjdc ewjhrg en vcjd c')
    print(caminho_dijkstra)

    if caminho is None:
        print('Sem caminho possível')
    else:
        print('Custo:', custo)
        print('Caminho:', caminho)
        desenhar(MAPA, caminho, custo)
        desenhar(MAPA, caminho_dijkstra, custo_digkstra)

if __name__ == '__main__':
    main()
