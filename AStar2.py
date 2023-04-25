#Imports dos mapas e das bibliotecas necessárias
import pygame
import time
from mapa import mapa
from dungeon1 import dungeon1
from dungeon2 import dungeon2
from dungeon3 import dungeon3
from queue import PriorityQueue


#Cores do mapa
CORES = {
    'Branco': (255,255,255),
    #Terrenos
    'Grama': (144,238,144), #Grama-> Verde Claro
    'Areia': (245,222,179), #Areia -> Marrom Claro
    'Floresta': (34,139,34), #Floresta -> Verde Escuro
    'Montanha': (139,69,19),  #Montanha -> Marrom escuro
    'Agua': (0,0,139), #Água -> Azul Escuro

    #Cores das dungeons
    'Parede': (139,69,19), #Marrom escuro
    'Caminho': (245,222,179), #Marrom Claro

    #Cores dos demais elementos
    'PortaDungeon': (0,0,0), #Preto
    'PingenteD1': (0,0,255), #Azul
    'PingenteD2': (0,255,0), #Verde
    'PingenteD3': (255,0,0), #Vermelho
    'Grade': (128, 128, 128), #Cinza
    'PontoPartida': (47,79,79), #Casa do Link -> Verde Acinzentado
    'PontoFinal': (192,192,192), #Master Sword -> Prata
    'CaminhoPercorrido': (255,165,0), #Caminho Final -> Laranja
}

#Globais
tela_criada = False
global tela
TAMANHO_CELULA = 15

#Inicializa o Pygame
pygame.init()

def Desenha_mapa(matriz_atual):
    global tela_criada
    global tela

    #Definição de valores do mapa principal
    linhas = 42
    colunas = 42

    #Propriedades da tela
    LARGURA_TELA = colunas * TAMANHO_CELULA
    ALTURA_TELA = linhas * TAMANHO_CELULA

    # Verifica tela criada
    if(tela_criada == False):
        tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        tela_criada = True

    dungeon_gate = pygame.image.load("img/dungeonGate.png").convert_alpha()
    dungeon_gate = pygame.transform.scale(dungeon_gate, (TAMANHO_CELULA, TAMANHO_CELULA))

    linkChar = pygame.image.load("img/linkChar.png").convert_alpha()
    linkChar = pygame.transform.scale(linkChar, (15, 15))

    masterSword = pygame.image.load("img/masterSword.png").convert_alpha()
    masterSword = pygame.transform.scale(masterSword, (15, 15))

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

            #Adiciona as sprites dos pontos de interesse
            if valor == 0: # Sprite Link
                posicao_x = linha * TAMANHO_CELULA
                posicao_y = coluna * TAMANHO_CELULA
                tela.blit(linkChar, (posicao_y, posicao_x))
                pygame.display.update()

            elif((valor == 1) or (valor == 2) or (valor == 3) or (valor == 4)): # Sprite Portas das Dungeons
                posicao_x = linha * TAMANHO_CELULA
                posicao_y = coluna * TAMANHO_CELULA
                tela.blit(dungeon_gate, (posicao_y, posicao_x))
                pygame.display.update()

            elif valor == 5: # Sprite Master Sword
                posicao_x = linha * TAMANHO_CELULA
                posicao_y = coluna * TAMANHO_CELULA
                tela.blit(masterSword, (posicao_y, posicao_x))
                pygame.display.update()

            #Chamadas das funções de desenho
            Desenha_celula(cor, linha, coluna, TAMANHO_CELULA)
            Desenha_linha(linha, coluna, TAMANHO_CELULA)

    pygame.display.update()


def Desenha_dungeon(matriz_atual):
    global tela_criada
    global tela

    #Definição de linhas e colunas das dungeons
    linhas = 28
    colunas= 28

    #Propriedades da tela
    LARGURA_TELA = colunas * TAMANHO_CELULA
    ALTURA_TELA = linhas * TAMANHO_CELULA


    # Criar a tela
    if(tela_criada == False):
        tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        tela_criada = True

    for linha in range(len(matriz_atual)):
        for coluna in range(len(matriz_atual[linha])):
            valor = matriz_atual[linha][coluna]
            if valor == 1000:
                cor = CORES['Parede']
            elif valor == 10:
                cor = CORES['Caminho']

            #Pintando a posição da porta e do pingente
            if(valor == 1):
                cor = CORES['PortaDungeon']

            if((matriz_atual == dungeon1) and (valor == 2)) :
                cor = CORES['PingenteD1']

            if((matriz_atual == dungeon2) and (valor == 2)) :
                cor = CORES['PingenteD2']

            if((matriz_atual == dungeon3) and (valor == 2)) :
                cor = CORES['PingenteD3']

            Desenha_celula(cor, linha, coluna, TAMANHO_CELULA)
            Desenha_linha(linha, coluna, TAMANHO_CELULA)

    pygame.display.update()


def Desenha_celula(cor, linha, coluna, TAMANHO_CELULA):
    pygame.draw.rect(tela, cor, (
                    coluna * TAMANHO_CELULA,
                    linha * TAMANHO_CELULA,
                    TAMANHO_CELULA,
                    TAMANHO_CELULA
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
    if x < len(matriz) - 1 and matriz[x+1][y] != 1:
        vizinhos.append((x+1, y))
    if x > 0 and matriz[x-1][y] != 1:
        vizinhos.append((x-1, y))
    if y < len(matriz[0]) - 1 and matriz[x][y+1] != 1:
        vizinhos.append((x, y+1))
    if y > 0 and matriz[x][y-1] != 1:
        vizinhos.append((x, y-1))
    return vizinhos


def algoritmo(matriz_atual, ponto1, ponto2):
    count = 0
    lista_aberta = PriorityQueue()
    lista_aberta.put((0, count, ponto1))
    caminho_percorrido = {}
    g_score = {(x, y): float("inf") for x in range(len(matriz_atual)) for y in range(len(matriz_atual[0]))}
    g_score[ponto1] = 0
    f_score = {(x, y): float("inf") for x in range(len(matriz_atual)) for y in range(len(matriz_atual[0]))}
    f_score[ponto1] = heuristica(ponto1, ponto2, matriz_atual)

    open_set_hash = {ponto1}

    while not lista_aberta.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        atual = lista_aberta.get()[2]
        open_set_hash.remove(atual)

        if atual == ponto2:
            break

        for vizinho in adiciona_vizinhos(matriz_atual, atual):
            temp_g_score = g_score[atual] + matriz_atual[vizinho[0]][vizinho[1]]

            if temp_g_score < g_score[vizinho]:
                caminho_percorrido[vizinho] = atual
                g_score[vizinho] = temp_g_score
                f_score[vizinho] = temp_g_score + heuristica(vizinho, ponto2, matriz_atual)
                if vizinho not in open_set_hash:
                    count += 1
                    lista_aberta.put((f_score[vizinho], count, vizinho))
                    open_set_hash.add(vizinho)

        if(matriz_atual == mapa):
            Desenha_mapa(matriz_atual)
            Desenha_caminho(matriz_atual, caminho_percorrido)
        else:
            Desenha_dungeon(matriz_atual)
            Desenha_caminho(matriz_atual, caminho_percorrido)

    if(matriz_atual == mapa):
        Desenha_mapa(matriz_atual)
        caminho_final = Gera_caminho(caminho_percorrido, ponto1, ponto2)
        Desenha_caminho(matriz_atual, caminho_final)
    else:
        Desenha_dungeon(matriz_atual)
        caminho_final = Gera_caminho(caminho_percorrido, ponto1, ponto2)
        Desenha_caminho(matriz_atual, caminho_final)


    time.sleep(20)
    return False


def Gera_caminho(caminho_percorrido, ponto1, ponto2):
    atual = ponto2
    caminho = [atual]

    while atual != ponto1:
        atual = caminho_percorrido[atual]
        caminho.append(atual)

    caminho.reverse()

    return caminho

def Desenha_caminho(matriz_atual, caminho_final):

    for linha in range(len(matriz_atual)):
        for coluna in range(len(matriz_atual[linha])):
            posicao = (linha, coluna)
            if posicao in caminho_final:
                cor = CORES['CaminhoPercorrido']
                Desenha_celula(cor, linha, coluna, TAMANHO_CELULA)
                Desenha_linha(linha, coluna, TAMANHO_CELULA)

    pygame.display.update()


pingenteD1Bool = False
pingenteD2Bool = False
pingenteD3Bool = False
masterSwordBool = False

run = True

while run:
    #Localização dos pontos de interesse
    ponto_origem = (27, 24) # Ponto 0
    portaD1 = (32, 5) # Ponto 1
    portaD2 = (17, 39) # Ponto 2
    portaD3 = (1,24) # Ponto 3
    ponto_destino = (5, 6) # Ponto 4

    entradaD1 = (26, 14)
    pingente1 = (3, 13)

    entradaD2 = (25, 13)
    pingente2 = (2, 13)

    entradaD3 = (25, 14)
    pingente3 = (19, 15)

    # Processar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

    # if(pingenteD1Bool == False):
    #     #Ponto de origem -> Porta Dungeon1
    #     algoritmo(mapa, ponto_origem, portaD1)
    #     # #Entrada da Dungeon1 -> Pingente 1
    #     # algoritmo(dungeon1, entradaD1, pingente1)
    #     # #Caminho inverso
    #     # algoritmo(dungeon1, pingente1, entradaD1)
    #     # pingenteD1Bool = True

    # if pingenteD2Bool == False:
    #     #Entrada Dungeon1 -> Entrdada Dungeon2
    #     algoritmo(mapa, portaD1, portaD2)
    #     #Entrada da Dungeon2 -> Pingente 2
    #     algoritmo(dungeon2, entradaD2, pingente2)
    #     #Caminho inverso
    #     algoritmo(dungeon2, pingente2, entradaD2)
    #     pingenteD2Bool = True

    # if pingenteD3Bool == False:
    #     #Entrada Dungeon2 -> Entrdada Dungeon3
    #     algoritmo(mapa, portaD2, portaD3)
    #     #Entrada da Dungeon3 -> Pingente 3
    #     algoritmo(dungeon3, entradaD3, pingente3)
    #     #Caminho inverso
    #     algoritmo(dungeon3, pingente3, entradaD3)
    #     pingenteD3Bool == True

    # if masterSwordBool == False:
    #     #Entrada Dungeon3 -> Ponto de destino
    #     algoritmo(mapa, portaD3, ponto_destino)
    #     masterSwordBool = True
    #     break

    #Desenha_mapa(mapa)
    #Desenha_dungeon(dungeon1)
    # ponto1 = (27,24)
    # ponto2 = (17,39)

    algoritmo(mapa, ponto_origem, portaD2)
    #break
