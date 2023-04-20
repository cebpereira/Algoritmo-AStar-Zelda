import pygame
from mapa import mapa
from dungeon1 import dungeon1
from dungeon2 import dungeon2
from dungeon3 import dungeon3

# Definir as constantes
LARGURA_TELA = 630
ALTURA_TELA = 630
TAMANHO_CELULA = 15
CORES = {
    #Cores do mapa
    'Grama': (144,238,144), #Grama-> Verde Claro
    'Areia': (245,222,179), #Areia -> Marron Claro
    'Floresta': (34,139,34), #Floresta -> Verde Escuro
    'Montanha': (139,69,19),  #Montanha -> Marrom escuro
    'Agua': (0,0,255), #Água -> Azul

    #Cores da dungeon
    'Parede': (139,69,19),
    'Caminho': (245,222,179)
}

# Inicializar o Pygame
pygame.init()

# Criar a tela
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

matriz_atual = dungeon3

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

                pygame.draw.rect(tela, cor, (
                    coluna * TAMANHO_CELULA,
                    linha * TAMANHO_CELULA,
                    TAMANHO_CELULA,
                    TAMANHO_CELULA
                ))

    elif((matriz_atual == dungeon1) or (matriz_atual == dungeon2) or (matriz_atual == dungeon3)):
        for linha in range(len(matriz_atual)):
            for coluna in range(len(matriz_atual[linha])):
                valor = matriz_atual[linha][coluna]
                if valor == 0:
                    cor = CORES["Parede"]
                elif valor == 10:
                    cor = CORES["Caminho"]

                pygame.draw.rect(tela, cor, (
                    coluna * TAMANHO_CELULA,
                    linha * TAMANHO_CELULA,
                    TAMANHO_CELULA,
                    TAMANHO_CELULA
                ))

    # Atualizar a tela
    pygame.display.update()
