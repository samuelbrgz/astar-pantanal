CUSTOS = {
    '.': 1,  # campo seco
    '~': 3,  # agua rasa
    '*': 5,  # lama/brejo
    'S': 1,  # inicio
    'G': 1,  # destino
}

MAPA = [
    'S....#.........',
    '..#..#..~~~~...',
    '..#....~~~~~~..',
    '......~~~JJ~~..',
    '###..~~~~~~~***',
    '....~~~~~~~*...',
    '..*~~~~~~**....',
    '..**~~~#.......',
    '.J..........#..',
    '......####....G',
]

def inifim(MAPA, simbolo):
    for i, linha in enumerate(MAPA):
        for j, coluna in enumerate(linha):
            if coluna == simbolo:
                return(i, j)

def movimentos(pos, MAPA, CUSTOS):
    linha, coluna = pos
    lista =  []
    if linha > 0:
        if (MAPA[linha -1][coluna] in CUSTOS):
            lista.append(((linha - 1, coluna), CUSTOS[MAPA[linha -1][coluna]]))
    if coluna > 0:
        if (MAPA[linha][coluna-1] in CUSTOS):
            lista.append(((linha, coluna -1), CUSTOS[MAPA[linha][coluna - 1]]))
        
    if linha < len(MAPA)-1:
        if (MAPA[linha + 1][coluna] in CUSTOS):
            lista.append(((linha + 1, coluna), CUSTOS[MAPA[linha + 1][coluna]]))
        
    if coluna < len(MAPA[0]) - 1:
         if (MAPA[linha][coluna + 1] in CUSTOS):
                    lista.append(((linha, coluna+1), CUSTOS[MAPA[linha][coluna+1]]))
    return lista

def manhattan(pos1, pos2):
     lin1, col1 = pos1
     lin2, col2 = pos2
     return (abs(lin1 - lin2) + abs(col1 - col2))
