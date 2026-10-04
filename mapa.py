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