from queue import PriorityQueue
import sys
import pygame
from mapa import mapa
from dungeon1 import dungeon1
from dungeon2 import dungeon2
from dungeon3 import dungeon3

import pygame

CORES = {
    'Grama': (144,238,144), #Grama
    'Areia': (245,222,179), #Areia 
    'Floresta': (34,139,34), #Floresta 
    'Montanha': (139,69,19),  #Montanha
    'Agua': (0,0,139), #Água 
    'Grade': (128, 128, 128),
    'PontoPartida': (47,79,79), #Casa do Link -> Verde Acinzentado
    'PontoFinal': (192,192,192), #Master Sword ->Prata
    'CaminhoFinal': (255,165,0) #Laranja
} 

# Inicializar o Pygame
pygame.init()

#Definição de valores do mapa principal
linhas = 42
colunas = 42
TAMANHO_CELULA = 15

#Propriedades da tela
LARGURA_TELA = colunas * TAMANHO_CELULA
ALTURA_TELA = linhas * TAMANHO_CELULA

# Criar a tela
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

matriz_atual = mapa

def h(start, end):  # Heurística - quanto falta para chegar no objetivo
  x1, y1 = start
  x2, y2 = end
  return abs(x1 + x2) + abs(y1 - y2)

def reconstruct_path(win, came_from, current, draw):
    list_path = [current]
    pygame.draw.rect(win, (255, 0, 0), (current.y, current.x, current.size, current.size))
    pygame.time.delay(100)
    while current in came_from:
        current = came_from[current]
        list_path.append(current)
        pygame.time.delay(60)
        draw()
        pygame.draw.rect(win, (255, 0, 0), (current.y, current.x, current.size, current.size))
        pygame.display.update()
    pygame.draw.rect(win, (255, 0, 0), (current.y, current.x, current.size, current.size))
    return list_path

# Algoritmo A*
def A_star(win, draw, map_points, start_point, end_point, best_way=False):
    came_from = {}
    count = 0

    # Lista aberta - nós a serem visitados
    open_set = {start_point}

    # Lista fechada - nós visitados
    closed_set = PriorityQueue()
    closed_set.put((0, count, start_point))

    # Quanto foi deslocado do nó inicial até o nó atual
    g_score = {point: float("inf") for row in map_points for point in row}
    g_score[start_point] = 0

    # Quanto falta deslocar do nó atual até o nó objetivo
    f_score = {point: float("inf") for row in map_points for point in row}
    f_score[start_point] = h(start_point.get_location(), end_point.get_location())

    # Executa o algoritmo enquanto a fila com vizinhos não visitados não for vazia
    while not closed_set.empty():

        # Sair do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        current = closed_set.get()[2]
        open_set.remove(current)

        list_path = []
        # Verifica se o nó atual é o objetivo, caso seja, ele constrói o caminho e retorna o caminho feito
        if current == end_point:
            if best_way == False:
                return list(reversed(reconstruct_path(win, came_from, current, draw)))
            else:
                list_path = [current]
                while current in came_from:
                    current = came_from[current]
                    list_path.append(current)
                return list(reversed(list_path))

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + neighbor.cost

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current

                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_location(), end_point.get_location())

                if neighbor not in open_set:
                    count += temp_g_score
                    closed_set.put((f_score[neighbor], count, neighbor))
                    open_set.add(neighbor)

# Loop principal do jogo
while True:
    # Processar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Desenhar a matriz na tela
    if(matriz_atual == mapa):
        for linha in range(len(matriz_atual)):
            for coluna in range(len(matriz_atual[linha])):
                valor = matriz_atual[linha][coluna]
                #Pintando terrenos do mapa
                if valor == 10:
                    cor = CORES['Grama']
                elif valor == 20:
                    cor = CORES['Areia']
                elif valor == 100:
                    cor = CORES['Floresta']
                elif valor == 150:
                    cor = CORES['Montanha']
                elif valor == 180:
                    cor = CORES['Agua']

                #Desenhando as células
                pygame.draw.rect(tela, cor, (
                    coluna * TAMANHO_CELULA,
                    linha * TAMANHO_CELULA,
                    TAMANHO_CELULA,
                    TAMANHO_CELULA
                ))

                #Desenhando as linhas da matriz
                pygame.draw.line(tela, CORES['Grade'], (coluna * TAMANHO_CELULA, linha * TAMANHO_CELULA),
                             ((coluna + 1) * TAMANHO_CELULA, linha * TAMANHO_CELULA))
                pygame.draw.line(tela, CORES['Grade'], (coluna * TAMANHO_CELULA, linha * TAMANHO_CELULA),
                             (coluna * TAMANHO_CELULA, (linha + 1) * TAMANHO_CELULA))

    #Atualizar a tela
    pygame.display.update()