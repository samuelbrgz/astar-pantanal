import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def desenhar(MAPA, caminho, custo):
    simbolos = ['.', '~', '*', '#', 'J', 'S', 'G']
    cores = ['#d9ead3', '#9fc5e8', '#7f6000', '#222222', '#e69138', '#38761d', '#f1c232']
    indice = {s: i for i, s in enumerate(simbolos)}

    matriz = [[indice[c] for c in linha] for linha in MAPA]

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.imshow(matriz, cmap=ListedColormap(cores), vmin=0, vmax=len(simbolos) - 1)

    ys = [p[0] for p in caminho]  # linha  -> eixo y
    xs = [p[1] for p in caminho]  # coluna -> eixo x
    ax.plot(xs, ys, color='magenta', linewidth=3, marker='o', markersize=5)

    ax.set_title(f'Caminho ideal - custo total: {custo}')
    ax.set_xticks(range(len(MAPA[0])))
    ax.set_yticks(range(len(MAPA)))
    ax.grid(color='white', linewidth=0.5)
    plt.show()