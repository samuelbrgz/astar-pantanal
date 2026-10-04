from mapa import MAPA, CUSTOS, inifim

def main():

    print('Mapa do Pantanal:')
    for i in range(len(MAPA)):
        print(MAPA[i])
    print(inifim(MAPA, 'S'), inifim(MAPA, 'G'))
        
if __name__ == '__main__':
    main()