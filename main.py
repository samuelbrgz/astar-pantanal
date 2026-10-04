import sys
print(sys.executable)

from mapa import MAPA, CUSTOS, inifim
from astar import astar
from visual import desenhar 

def main():
    inicio = inifim(MAPA, 'S')
    fim = inifim(MAPA, 'G')

    custo, caminho = astar(inicio, fim, MAPA, CUSTOS)

    if caminho is None:
        print('Sem caminho possível')
    else:
        print('Custo:', custo)
        print('Caminho:', caminho)
        desenhar(MAPA, caminho, custo)

if __name__ == '__main__':
    main()