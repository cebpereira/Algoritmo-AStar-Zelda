import pygame
from dungeon1 import dungeon1

# Define o tamanho de cada tile
TILE_SIZE = 32

# Define as cores dos tiles
WALL_COLOR = (139, 69, 19)  # azul
PATH_COLOR = (245, 222, 179)  # branco

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

# Inicializa o Pygame
pygame.init()

# Define a janela do jogo
screen = pygame.display.set_mode(
    (len(dungeon[0]) * TILE_SIZE, len(dungeon) * TILE_SIZE))

# Loop do jogo
while True:
    # Processa eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Desenha os tiles
    tiles.draw(screen)

    # Desenhando as linhas da matriz
    for i in range(len(dungeon) + 1):
        pygame.draw.line(screen, (128, 128, 128), (0, i * TILE_SIZE),
                         (len(dungeon[0]) * TILE_SIZE, i * TILE_SIZE))
    for j in range(len(dungeon[0]) + 1):
        pygame.draw.line(screen, (128, 128, 128), (j * TILE_SIZE, 0),
                         (j * TILE_SIZE, len(dungeon) * TILE_SIZE))

    # Atualiza a tela
    pygame.display.flip()
