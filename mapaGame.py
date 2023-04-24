import heapq
import sys
import pygame
from mapa import mapa

# Definindo as cores
GRAMA = (144, 238, 144)
AREIA = (245, 222, 179)
FLORESTA = (34, 139, 34)
MONTANHA = (139, 69, 19)
AGUA = (0, 0, 139)
YELLOW = (128, 128, 128)
RED = (255, 0, 0)

CaminhoFinal = (255, 165, 0)

# Definindo as dimensões dos retângulos
RECT_WIDTH = 16
RECT_HEIGHT = 16

LINE_WIDTH = 1
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700


def draw_map(screen, dungeon, ):
    for row in range(len(dungeon)):
        for col in range(len(dungeon[0])):
            if dungeon[row][col] == 0:
                pygame.draw.rect(
                    screen, RED, (col * RECT_WIDTH, row * RECT_HEIGHT, RECT_WIDTH, RECT_HEIGHT))
            elif dungeon[row][col] == 10:
                pygame.draw.rect(
                    screen, GRAMA, (col * RECT_WIDTH, row * RECT_HEIGHT, RECT_WIDTH, RECT_HEIGHT))
            elif dungeon[row][col] == 20:
                pygame.draw.rect(
                    screen, AREIA, (col * RECT_WIDTH, row * RECT_HEIGHT, RECT_WIDTH, RECT_HEIGHT))
            elif dungeon[row][col] == 100:
                pygame.draw.rect(
                    screen, FLORESTA, (col * RECT_WIDTH, row * RECT_HEIGHT, RECT_WIDTH, RECT_HEIGHT))
            elif dungeon[row][col] == 150:
                pygame.draw.rect(
                    screen, MONTANHA, (col * RECT_WIDTH, row * RECT_HEIGHT, RECT_WIDTH, RECT_HEIGHT))
            elif dungeon[row][col] == 180:
                pygame.draw.rect(
                    screen, AGUA, (col * RECT_WIDTH, row * RECT_HEIGHT, RECT_WIDTH, RECT_HEIGHT))

    # Desenha as linhas verticais
    for col in range(len(dungeon[0])+1):
        pygame.draw.line(screen, YELLOW, (col*RECT_WIDTH, 0),
                         (col*RECT_WIDTH, SCREEN_HEIGHT), LINE_WIDTH)

    # Desenha as linhas horizontais
    for row in range(len(dungeon)+1):
        pygame.draw.line(screen, YELLOW, (0, row*RECT_HEIGHT),
                         (SCREEN_WIDTH, row*RECT_HEIGHT), LINE_WIDTH)


def distancia_manhattan(pos1, pos2):
    """
    Calcula a distância Manhattan entre duas posições no grid.

    Args:
        pos1 (tuple): posição 1 no formato (linha, coluna)
        pos2 (tuple): posição 2 no formato (linha, coluna)

    Returns:
        int: distância Manhattan entre as duas posições
    """
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def obter_vizinhos(no_atual, mapa):
    vizinhos = []
    for direcao in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        linha_vizinha = no_atual[0] + direcao[0]
        coluna_vizinha = no_atual[1] + direcao[1]
        if linha_vizinha < 0 or coluna_vizinha < 0 or linha_vizinha >= len(mapa) or coluna_vizinha >= len(mapa[0]):
            continue  # A vizinhança está fora do mapa, então não pode ser um vizinho
        if mapa[linha_vizinha][coluna_vizinha] == 0:
            continue  # O vizinho é um obstáculo, então não pode ser um vizinho
        custo_vizinho = None
        if mapa[linha_vizinha][coluna_vizinha] == 10:
            custo_vizinho = 10
        elif mapa[linha_vizinha][coluna_vizinha] == 20:
            custo_vizinho = 20
        elif mapa[linha_vizinha][coluna_vizinha] == 100:
            custo_vizinho = 100
        elif mapa[linha_vizinha][coluna_vizinha] == 150:
            custo_vizinho = 150
        elif mapa[linha_vizinha][coluna_vizinha] == 180:
            custo_vizinho = 180
        if custo_vizinho is not None:
            vizinhos.append(((linha_vizinha, coluna_vizinha), custo_vizinho))
    return vizinhos


def a_star(mapa, inicio, objetivo):
    fronteira = []
    heapq.heappush(fronteira, (0, inicio))
    came_from = {}
    custo_g = {}
    came_from[inicio] = None
    custo_g[inicio] = 0

    while len(fronteira) > 0:
        _, no_atual = heapq.heappop(fronteira)
        if no_atual == objetivo:
            break
        vizinhos = obter_vizinhos(no_atual, mapa)
        for vizinho, custo in vizinhos:
            novo_custo_g = custo_g[no_atual] + custo
            if vizinho not in custo_g or novo_custo_g < custo_g[vizinho]:
                custo_g[vizinho] = novo_custo_g
                prioridade = novo_custo_g + \
                    distancia_manhattan(vizinho, objetivo)
                heapq.heappush(fronteira, (prioridade, vizinho))
                came_from[vizinho] = no_atual

    if objetivo not in came_from:
        return None
    caminho = [objetivo]
    while caminho[-1] != inicio:
        caminho.append(came_from[caminho[-1]])
    caminho.reverse()
    return caminho


# Inicializa o pygame
pygame.init()

# Cria a janela do jogo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo")

# Define a posição inicial e final do jogador
posicao_jogador = (24, 27)

posicao_final = (1, 23)
# for row in range(len(mapa)):
# for col in range(len(mapa[0])):
# if mapa[row][col] == "PortaDungeon":
# posicao_final = (col, row)


def draw_path(screen, path, color):
    for node in path:
        row, col = node
        pygame.draw.rect(
            screen, color, (col * RECT_WIDTH, row * RECT_HEIGHT, RECT_WIDTH, RECT_HEIGHT))
        pygame.display.update()
        pygame.time.delay(100)


def draw_path2(screen, path):
    for i in range(len(path)):
        node = path[i]
        pygame.draw.rect(screen, CaminhoFinal, (node[0] * RECT_WIDTH + LINE_WIDTH, node[1] * RECT_HEIGHT + LINE_WIDTH,
                                                RECT_WIDTH - LINE_WIDTH * 2, RECT_HEIGHT - LINE_WIDTH * 2))
        # Desenha a tela a cada iteração do loop
        pygame.display.update()
        pygame.time.delay(100)  # Adiciona um atraso de 100 milissegundos

        # Verifica se o nó atual é o objetivo final
        if node == path[-1]:
            # Espera uma tecla ser pressionada para continuar
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        return


# Executa o loop principal do jogo
while True:
    # Processa eventos de entrada do usuário
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpa a tela
    screen.fill(YELLOW)

    # Desenha o mapa
    draw_map(screen, mapa)

    # Desenha o jogador
    pygame.draw.circle(screen, CaminhoFinal, (posicao_jogador[1] * RECT_WIDTH + RECT_WIDTH // 2,
                                              posicao_jogador[0] * RECT_HEIGHT + RECT_HEIGHT // 2), RECT_WIDTH // 2)

    # Executa um passo do algoritmo A*
    caminho = a_star(mapa, posicao_jogador, posicao_final)

    # Desenha o caminho final
    if caminho:
        draw_path(screen, caminho, CaminhoFinal)

    draw_path2(screen, caminho)
    # Move o jogador para a próxima posição no caminho
    if len(caminho) > 1:
        posicao_jogador = caminho[1]

    # Atualiza a tela
    pygame.display.update()
