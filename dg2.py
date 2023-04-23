from queue import PriorityQueue
import pygame
from dungeon1 import dungeon1
from heapq import heappush, heappop

# Define o tamanho de cada tile
TILE_SIZE = 32

# Define as cores dos tiles
WALL_COLOR = (139, 69, 19)  # azul
PATH_COLOR = (245, 222, 179)  # branco
PATH_COLOR_RED = (255, 0, 0)  # vermelho


# Define a matriz
dungeon = dungeon1


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE


# Cria o grupo de sprites
tiles = pygame.sprite.Group()

# Percorre a matriz e cria os tiles
for y, row in enumerate(dungeon):
    for x, tile in enumerate(row):
        if tile == 0:
            tiles.add(Tile(x, y, WALL_COLOR))
        elif tile == 10:
            tiles.add(Tile(x, y, PATH_COLOR))

# Função de busca A*


class Graph:
    def __init__(self, dungeon):
        self.nodes = {}
        self.neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for y, row in enumerate(dungeon):
            for x, tile in enumerate(row):
                if tile != 0:
                    self.nodes[(x, y)] = set()
                    for dx, dy in self.neighbors:
                        neighbor = (x + dx, y + dy)
                        if neighbor in self.nodes:
                            self.nodes[(x, y)].add(neighbor)
                            self.nodes[neighbor].add((x, y))

    def get_neighbors(self, node):
        return self.nodes[node]

    def get_cost(self, current, neighbor):
        return 1


def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


def get_neighbors(node, dungeon):
    x, y = node
    neighbors = []
    if x > 0 and not dungeon[x-1][y]:
        neighbors.append((x-1, y))
    if y > 0 and not dungeon[x][y-1]:
        neighbors.append((x, y-1))
    if x < len(dungeon)-1 and not dungeon[x+1][y]:
        neighbors.append((x+1, y))
    if y < len(dungeon[0])-1 and not dungeon[x][y+1]:
        neighbors.append((x, y+1))
    return neighbors


def get_cost(node, neighbor):
    return 1


def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for neighbor in graph.nodes[current]:
            new_cost = cost_so_far[current] + graph.get_cost(current, neighbor)
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(goal, neighbor)
                frontier.put(neighbor, priority)
                came_from[neighbor] = current

    path = reconstruct_path(came_from, start, goal)
    return path


# Inicializa o Pygame
pygame.init()

# Define a janela do jogo
screen = pygame.display.set_mode(
    (len(dungeon[0]) * TILE_SIZE, len(dungeon) * TILE_SIZE))

# Define os pontos de início e destino da busca
start = (13, 3)
goal = (14, 26)

# Executa a busca A*
path = a_star_search(Graph(dungeon), start, goal)

# Cria o grupo de sprites para o caminho encontrado
path_tiles = pygame.sprite.Group()
path_tiles_red = pygame.sprite.Group()


# Cria os tiles para o caminho encontrado
for tile in path:
    path_tiles.add(Tile(tile[0], tile[1], PATH_COLOR))

for tile in path:
    path_tiles_red.add(Tile(tile[0], tile[1], PATH_COLOR_RED))


# Loop do jogo
while True:
    # Processa eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Desenha os tiles
    tiles.draw(screen)
    path_tiles.draw(screen)
    path_tiles_red.draw(screen)

    # Desenhando as linhas da matriz
    for i in range(len(dungeon) + 1):
        pygame.draw.line(screen, (128, 128, 128), (0, i * TILE_SIZE),
                         (len(dungeon[0]) * TILE_SIZE, i * TILE_SIZE))
    for j in range(len(dungeon[0]) + 1):
        pygame.draw.line(screen, (128, 128, 128), (j * TILE_SIZE, 0),
                         (j * TILE_SIZE, len(dungeon) * TILE_SIZE))

    # Atualiza a tela
    pygame.display.flip()
