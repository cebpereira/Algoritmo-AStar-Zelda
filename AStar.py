import pygame
import math
from queue import PriorityQueue

#Configurações da janela
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Zelda com Algoritmo A*")

#Cores dos Elementos do Mapa
AguaCor = (0,0,255) #Água -> Azul
GramaCor = (144,238,144) #Grama-> Verde Claro
FlorestaCor = (34,139,34) #Floresta -> Verde Escuro
AreiaCor = (245,222,179) #Areia -> Marron Claro
MontanhaCor = (139,69,19) #Montanha -> Marrom Escuro
EntradaMasmorraCor = (0,0,0) #Entrada da masmorra -> Preto

#Cores relacionadas aos caminhos
CaminhoCor = (128,0,128) #Cor do Caminho -> Roxo

#Status das masmorras, pingentes e da Espada
Masmorra1 = False #[6,33]
Masmorra2 = False #[40,18]
Masmorra3 = False #[25,2]
MasterSword = False #[3,2]
PingenteD1 = False
PingenteD2 = False
PingenteD3 = False


class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows


    #Elementos
    def is_water(self):
        return self.color == AguaCor
    
    def is_grass(self):
        return self.color == GramaCor
    
    def is_forest(self):
        return self.color == FlorestaCor
    
    def is_sand(self):
        return self.color == AreiaCor
    
    def is_mountain(self):
        return self.color == MontanhaCor