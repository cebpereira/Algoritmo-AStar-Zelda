# Imports dos mapas e das bibliotecas necessárias
import pygame
import time
from mapa import mapa
from dungeon1 import dungeon1
from dungeon2 import dungeon2
from dungeon3 import dungeon3
from queue import PriorityQueue


# Cores do mapa
CORES = {
    'Grade': (128, 128, 128), # Cinza
}

# Globais
tela_criada = False
global tela
TAMANHO_CELULA = 15

# Inicializa o Pygame
pygame.init()

def Desenha_mapa(matriz_atual):
    global tela_criada
    global tela

    # Definição de valores do mapa principal
    linhas = 42
    colunas = 42

    # Propriedades da tela
    LARGURA_TELA = colunas * TAMANHO_CELULA
    ALTURA_TELA = linhas * TAMANHO_CELULA

    # Verifica tela criada
    if(tela_criada == False):
        tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        tela_criada = True


    # Percorre a matriz atribuindo cor e pintando os elementos do mapa
    for linha in range(len(matriz_atual)):
        for coluna in range(len(matriz_atual[linha])):
            valor = matriz_atual[linha][coluna]
            # Pintando terrenos do mapa
            if valor == 10:
                sprite = pygame.image.load("img/grama_sprite.png").convert_alpha()
                sprite = pygame.transform.scale(sprite, (TAMANHO_CELULA, TAMANHO_CELULA))
                pygame.display.update()
            elif valor == 20:
                sprite = pygame.image.load("img/areia_sprite.png").convert_alpha()
                sprite = pygame.transform.scale(sprite, (TAMANHO_CELULA, TAMANHO_CELULA))
                pygame.display.update()
            elif valor == 100:
                sprite = pygame.image.load("img/floresta_sprite.png").convert_alpha()
                sprite = pygame.transform.scale(sprite, (TAMANHO_CELULA, TAMANHO_CELULA))
                pygame.display.update()
            elif valor == 150:
                sprite = pygame.image.load("img/montanha_sprite.png").convert_alpha()
                sprite = pygame.transform.scale(sprite, (TAMANHO_CELULA, TAMANHO_CELULA))
                pygame.display.update()
            elif valor == 180:
                sprite = pygame.image.load("img/agua_sprite.png").convert_alpha()
                sprite = pygame.transform.scale(sprite, (TAMANHO_CELULA, TAMANHO_CELULA))
                pygame.display.update()

            # Adiciona pontos de interesse
            elif valor == 99:
                sprite = pygame.image.load("img/casa_sprite.png").convert_alpha()
                sprite = pygame.transform.scale(sprite, (TAMANHO_CELULA, TAMANHO_CELULA))
                pygame.display.update()

            elif((valor == 98) or (valor == 97) or (valor == 96) or (valor == 95)):
                sprite = pygame.image.load("img/dungeon_gate.png").convert_alpha()
                sprite = pygame.transform.scale(sprite, (TAMANHO_CELULA, TAMANHO_CELULA))
                pygame.display.update()

            elif valor == 94:
                sprite = pygame.image.load("img/master_sword.png").convert_alpha()
                sprite = pygame.transform.scale(sprite, (TAMANHO_CELULA, TAMANHO_CELULA))
                pygame.display.update()

            # Chamada das funções de desenho
            Desenha_sprite(sprite, linha, coluna)
            Desenha_linha(linha, coluna, TAMANHO_CELULA)

    pygame.display.update()


def Desenha_dungeon(matriz_atual):
    global tela_criada
    global tela

    # Definição de linhas e colunas das dungeons
    linhas = 28
    colunas= 28

    # Propriedades da tela
    LARGURA_TELA = colunas * TAMANHO_CELULA
    ALTURA_TELA = linhas * TAMANHO_CELULA


    # Criar a tela
    if(tela_criada == False):
        tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        tela_criada = True


    # Percorre a matriz atribuindo cor e pintando os elementos do mapa
    for linha in range(len(matriz_atual)):
        for coluna in range(len(matriz_atual[linha])):
            valor = matriz_atual[linha][coluna]
            if valor == 0:
                sprite = pygame.image.load("img/montanha_sprite.png").convert_alpha()
                sprite = pygame.transform.scale(sprite, (TAMANHO_CELULA, TAMANHO_CELULA))
                pygame.display.update()
            elif valor == 10:
                sprite = pygame.image.load("img/areia_sprite.png").convert_alpha()
                sprite = pygame.transform.scale(sprite, (TAMANHO_CELULA, TAMANHO_CELULA))
                pygame.display.update()

            # Pintando a posição da porta e do pingente
            if(valor == 1):
                sprite = pygame.image.load("img/dungeon_gate.png").convert_alpha()
                sprite = pygame.transform.scale(sprite, (TAMANHO_CELULA, TAMANHO_CELULA))
                pygame.display.update()

            elif((matriz_atual == dungeon1) and (valor == 2)) :
                sprite = pygame.image.load("img/pingente1.png").convert_alpha()
                sprite = pygame.transform.scale(sprite, (TAMANHO_CELULA, TAMANHO_CELULA))
                pygame.display.update()

            elif((matriz_atual == dungeon2) and (valor == 2)) :
                sprite = pygame.image.load("img/pingente2.png").convert_alpha()
                sprite = pygame.transform.scale(sprite, (TAMANHO_CELULA, TAMANHO_CELULA))
                pygame.display.update()

            elif((matriz_atual == dungeon3) and (valor == 2)) :
                sprite = pygame.image.load("img/pingente3.png").convert_alpha()
                sprite = pygame.transform.scale(sprite, (TAMANHO_CELULA, TAMANHO_CELULA))
                pygame.display.update()

            # Chamada das funções de desenho
            Desenha_sprite(sprite, linha, coluna)
            Desenha_linha(linha, coluna, TAMANHO_CELULA)

    pygame.display.update()


def Desenha_sprite(sprite, linha, coluna):
    tela.blit(sprite, (
                    coluna * TAMANHO_CELULA,
                    linha * TAMANHO_CELULA,
                ))


def Desenha_linha(linha, coluna, TAMANHO_CELULA):
    pygame.draw.line(tela, CORES['Grade'], (coluna * TAMANHO_CELULA, linha * TAMANHO_CELULA),
                             ((coluna + 1) * TAMANHO_CELULA, linha * TAMANHO_CELULA))
    pygame.draw.line(tela, CORES['Grade'], (coluna * TAMANHO_CELULA, linha * TAMANHO_CELULA),
                             (coluna * TAMANHO_CELULA, (linha + 1) * TAMANHO_CELULA))


def heuristica(ponto1, ponto2, matriz_atual):
	x1, y1 = ponto1
	x2, y2 = ponto2
	return abs(x1 - x2) + abs(y1 - y2) + int(matriz_atual[x2][y2])


def adiciona_vizinhos(matriz, pos):
    vizinhos = []
    x, y = pos
    if x < len(matriz) - 1 and matriz[x+1][y] != 0: # Verifica Direita
        vizinhos.append((x+1, y))
    if x > 0 and matriz[x-1][y] != 0:   # Verifica Esquerda
        vizinhos.append((x-1, y))
    if y < len(matriz[0]) - 1 and matriz[x][y+1] != 0: # Verifica Baixo
        vizinhos.append((x, y+1))
    if y > 0 and matriz[x][y-1] != 0:   # Verifica Cima
        vizinhos.append((x, y-1))
    return vizinhos


def algoritmo(matriz_atual, ponto1, ponto2):
    count = 0
    lista_fechada = PriorityQueue()
    lista_fechada.put((0, count, ponto1))
    caminho_percorrido = {}
    g = {(x, y): float("inf") for x in range(len(matriz_atual)) for y in range(len(matriz_atual[0]))} # Custo percorrido até o momento
    g[ponto1] = 0
    f = {(x, y): float("inf") for x in range(len(matriz_atual)) for y in range(len(matriz_atual[0]))} # Custo total -> F(n) = G(n) + H(n)
    f[ponto1] = heuristica(ponto1, ponto2, matriz_atual)

    lista_aberta = {ponto1}

    while not lista_fechada.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        atual = lista_fechada.get()[2] # Ponto atual da lista fechada com menor prioridade
        lista_aberta.remove(atual)

        if atual == ponto2: # Destino -> Finaliza o loop
            break

        for vizinho in adiciona_vizinhos(matriz_atual, atual):
            temp_g = g[atual] + matriz_atual[vizinho[0]][vizinho[1]] # Custo até o vizinho

            if temp_g < g[vizinho]: # Se novo custo menor que custo até vizinho
                caminho_percorrido[vizinho] = atual # Atualiza o caminho até o vizinho
                g[vizinho] = temp_g # Atualiza o custo até o vizinho
                f[vizinho] = temp_g + heuristica(vizinho, ponto2, matriz_atual) # Atualiza o custo total
                if vizinho not in lista_aberta: # Fora da lista aberta
                    count += 1
                    lista_fechada.put((f[vizinho], count, vizinho)) # Adiciona a lista fechada com prioridade f[vizinho]
                    lista_aberta.add(vizinho)

        print("Custo Atual: ", g[atual])

    # Verifica a matriz utilizada
    if(matriz_atual == mapa):
        Desenha_mapa(matriz_atual)
        caminho_final = Gera_caminho(caminho_percorrido, ponto1, ponto2)
        Desenha_caminho(caminho_final)
    else:
        Desenha_dungeon(matriz_atual)
        caminho_final = Gera_caminho(caminho_percorrido, ponto1, ponto2)
        Desenha_caminho(caminho_final)

    print("Custo Final: ", g[ponto2])
    time.sleep(3)
    return False

# Gera o caminho a partir da lista de caminho percorrido/visitado
def Gera_caminho(caminho_percorrido, ponto1, ponto2):
    atual = ponto2
    caminho = [atual]

    while atual != ponto1:
        atual = caminho_percorrido[atual]
        caminho.append(atual)

    caminho.reverse()

    return caminho

# Desenha o caminho final utilizando sprite
def Desenha_caminho(caminho_final):
    sprite = pygame.image.load("img/link_char.png").convert_alpha()
    sprite = pygame.transform.scale(sprite, (TAMANHO_CELULA, TAMANHO_CELULA))

    for i, (linha, coluna) in enumerate(caminho_final):
        Desenha_sprite(sprite, linha, coluna)
        Desenha_linha(linha, coluna, TAMANHO_CELULA)
        pygame.display.update()
        pygame.time.delay(50)


# loop principal
while True:
    #Localização dos pontos de interesse no mapa
    ponto_origem = (27, 24) # Ponto 99
    portaD1 = (32, 5) # Ponto 98
    portaD2 = (17, 39) # Ponto 97
    portaD3 = (1,24) # Ponto 96
    ponto_destino = (5, 6) # Ponto 95

    # Pontos de entrada/saída e pingentes das dungeons
    entradaD1 = (26, 14)
    pingente1 = (3, 13)

    entradaD2 = (25, 13)
    pingente2 = (2, 13)

    entradaD3 = (25, 14)
    pingente3 = (19, 15)

    # Processar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.time.Clock().tick(60)

    ###### Fluxo de busca de caminhos

    #Ponto de origem -> Porta Dungeon1
    algoritmo(mapa, ponto_origem, portaD1)
    tela_criada = False
    #Entrada da Dungeon1 -> Pingente 1
    algoritmo(dungeon1, entradaD1, pingente1)
    tela_criada = False
    #Caminho inverso
    algoritmo(dungeon1, pingente1, entradaD1)
    tela_criada = False


    #Entrada Dungeon1 -> Entrdada Dungeon2
    algoritmo(mapa, portaD1, portaD2)
    tela_criada = False
    #Entrada da Dungeon2 -> Pingente 2
    algoritmo(dungeon2, entradaD2, pingente2)
    tela_criada = False
    #Caminho inverso
    algoritmo(dungeon2, pingente2, entradaD2)
    tela_criada = False

    #Entrada Dungeon2 -> Entrdada Dungeon3
    algoritmo(mapa, portaD2, portaD3)
    tela_criada = False
    #Entrada da Dungeon3 -> Pingente 3
    algoritmo(dungeon3, entradaD3, pingente3)
    tela_criada = False
    #Caminho inverso
    algoritmo(dungeon3, pingente3, entradaD3)
    tela_criada = False

    #Entrada Dungeon3 -> Ponto de destino
    algoritmo(mapa, portaD3, ponto_destino)
    break

