#Imports dos mapas e das bibliotecas necessárias
import pygame
from mapa import mapa
from dungeon1 import dungeon1
from dungeon2 import dungeon2
from dungeon3 import dungeon3
from queue import PriorityQueue

#Cores do mapa
CORES = {
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
    'PontoFinal': (192,192,192), #Master Sword ->Prata
    'CaminhoFinal': (255,165,0) #Laranja
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

            #Pintando pontos de interesse
            if valor == 'PortaDungeon':
                cor = CORES['PortaDungeon']
            if valor == 'PontoPartida':
                cor = CORES['PontoPartida']
            if valor == 'PontoFinal':
                cor = CORES['PontoFinal']

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
            if valor == 0:
                cor = CORES['Parede']
            elif valor == 10:
                cor = CORES['Caminho']

            #Pintando a posição da porta e do pingente
            if(valor == 'PortaDungeon'):
                cor = CORES['PortaDungeon']

            if((matriz_atual == dungeon1) and (valor == 'PingenteD1')) :
                cor = CORES['PingenteD1']

            if((matriz_atual == dungeon2) and (valor == 'PingenteD2')) :
                cor = CORES['PingenteD2']

            if((matriz_atual == dungeon3) and (valor == 'PingenteD3')) :
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

while True:
    # Processar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    Desenha_mapa(mapa)
    #Desenha_dungeon(dungeon1)
