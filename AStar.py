#Imports dos mapas e das bibliotecas necessárias
import pygame
from mapa import mapa
from dungeon1 import dungeon1
from dungeon2 import dungeon2
from dungeon3 import dungeon3

# Definir as constantes
TAMANHO_CELULA = 15
linhas = 42
colunas= 42

LARGURA_TELA = colunas * TAMANHO_CELULA
ALTURA_TELA = linhas * TAMANHO_CELULA


#Cores do mapa
CORES = {
    'Grama': (144,238,144), #Grama-> Verde Claro
    'Areia': (245,222,179), #Areia -> Marron Claro
    'Floresta': (34,139,34), #Floresta -> Verde Escuro
    'Montanha': (139,69,19),  #Montanha -> Marrom escuro
    'Agua': (0,0,139), #Água -> Azul Escuro

    #Cores das dungeons
    'Parede': (139,69,19),
    'Caminho': (245,222,179),

    #Cores dos demais elementos
    'PortaDungeon': (0,0,0),
    'PingenteD1': (0,0,255),
    'PingenteD2': (0,255,0),
    'PingenteD3': (255,0,0),
    'Grade': (128, 128, 128)
}

# Inicializar o Pygame
pygame.init()

matriz_atual = mapa

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

# Loop principal do jogo
while True:
    # Processar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Desenhar a matriz na tela
    if(matriz_atual == mapa):
        #Definição de valores do mapa principal
        #linhas = 42
        #colunas= 42
        #TAMANHO_CELULA = 15

        #Propriedades da tela
        #LARGURA_TELA = colunas * TAMANHO_CELULA
        #ALTURA_TELA = linhas * TAMANHO_CELULA

        # Criar a tela
        #tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

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

                #Pintando entradas das dungeons
                if valor == 'PortaDungeon':
                    cor = CORES['PortaDungeon']

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

    elif((matriz_atual == dungeon1) or (matriz_atual == dungeon2) or (matriz_atual == dungeon3)):
        #Definição de linhas e colunas das dungeons
        #linhas = 28
        #colunas= 28
        #TAMANHO_CELULA = 15

        #Propriedades da tela
        #LARGURA_TELA = colunas * TAMANHO_CELULA
        #ALTURA_TELA = linhas * TAMANHO_CELULA


        # Criar a tela
        #tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

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

    # Atualizar a tela
    pygame.display.update()
