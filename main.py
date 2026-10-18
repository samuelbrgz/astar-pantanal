import sys
from gerador import gerar_mapa
print(sys.executable)

from mapa import CUSTOS, inifim
from astar import astar
from visual import desenhar
from Dijkstra import Dijkstra
from BuscaExaustiva import Buscaexaustiva

def main():
    MAPA = gerar_mapa(linhas=12, colunas=12)
    inicio = inifim(MAPA, 'S')
    fim = inifim(MAPA, 'G')

    custo, caminho = astar(inicio, fim, MAPA, CUSTOS)
    custo_digkstra, caminho_dijkstra = Dijkstra(inicio, fim, MAPA, CUSTOS)
    custo_exaustiva, caminho_exaustiva = Buscaexaustiva(inicio, fim, MAPA, CUSTOS)



    if caminho is None or caminho_dijkstra is None or caminho_exaustiva is None:
        print('Sem caminho possível')
    else:
        print('Custo:', custo)
        print('Caminho:', caminho)
        desenhar(MAPA, caminho, custo)
        desenhar(MAPA, caminho_dijkstra, custo_digkstra)
        desenhar(MAPA, caminho_exaustiva, custo_exaustiva)

if __name__ == '__main__':
    main()
