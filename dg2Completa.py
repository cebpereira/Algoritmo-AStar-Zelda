import sys
import pygame
from dungeon2 import dungeon2
from math import floor
import heapq

# Define as cores
BLACK = (139, 69, 19)
GRAY = (245, 222, 179)
WHITE = (128, 128, 128)
CaminhoFinal = (255, 165, 0)

# Define as dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define as dimensões dos retângulos
RECT_WIDTH = round(SCREEN_WIDTH / len(dungeon2[0]))
RECT_HEIGHT = floor(SCREEN_HEIGHT / len(dungeon2))

# Define a largura das linhas
LINE_WIDTH = 2

# Cria a função que desenha o mapa na tela


def draw_map(screen, dungeon, ):
    for row in range(len(dungeon)):
        for col in range(len(dungeon[0])):
            if dungeon[row][col] == 0:
                pygame.draw.rect(
                    screen, BLACK, (col * RECT_WIDTH, row * RECT_HEIGHT, RECT_WIDTH, RECT_HEIGHT))
            elif dungeon[row][col] == 10:
                pygame.draw.rect(
                    screen, GRAY, (col * RECT_WIDTH, row * RECT_HEIGHT, RECT_WIDTH, RECT_HEIGHT))

    # Desenha as linhas verticais
    for col in range(len(dungeon[0])+1):
        pygame.draw.line(screen, WHITE, (col*RECT_WIDTH, 0),
                         (col*RECT_WIDTH, SCREEN_HEIGHT), LINE_WIDTH)

    # Desenha as linhas horizontais
    for row in range(len(dungeon)+1):
        pygame.draw.line(screen, WHITE, (0, row*RECT_HEIGHT),
                         (SCREEN_WIDTH, row*RECT_HEIGHT), LINE_WIDTH)

# Define a função de heurística


# Define a função heurística
def heuristic(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

# Define a função de custo


def cost(current, next):
    return 1

# Define a função de busca A*


def a_star(start, goal, dungeon):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while frontier:
        current = heapq.heappop(frontier)[1]

        if current == goal:
            break

        for next in get_neighbors(current, dungeon):
            new_cost = cost_so_far[current] + cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                heapq.heappush(frontier, (priority, next))
                came_from[next] = current

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    return path


def get_neighbors(node, dungeon):
    neighbors = []

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x = node[0] + dx
        y = node[1] + dy

        if x >= 0 and x < len(dungeon[0]) and y >= 0 and y < len(dungeon) and dungeon[y][x] != 0:
            neighbors.append((x, y))

    return neighbors

# Define a função que desenha o caminho na tela


# Define a função que desenha o caminho na tela
def draw_path(screen, path):
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


# Define o objetivo
goal = None
for row in range(len(dungeon2)):
    for col in range(len(dungeon2[0])):
        if dungeon2[row][col] == "PingenteD2":
            goal = (col, row)

# Define a posição inicial
start = (13, 25)

# Chama a função A*
path = a_star(start, goal, dungeon2)

# Inicializa o pygame
pygame.init()

# Cria a janela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Loop principal do jogo
while True:
    # Verifica se o usuário clicou no botão de fechar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Desenha o mapa na tela chamando a função
    draw_map(screen, dungeon2)

    # Desenha o caminho na tela chamando a função
    draw_path(screen, path)

    # Atualiza a tela
    pygame.display.flip()
