import pygame

# For now, I am using fake data for the ui
WIDTH, HEIGHT = 400, 400
TILE_SIZE = 40
ROWS, COLS = 10, 10

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def draw_grid(game_matrix):
    for r in range(ROWS):
        for c in range(COLS):
            rect = pygame.Rect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, (200, 200, 200), rect, 1)
#             grate logic here

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // TILE_SIZE, x // TILE_SIZE
    #         some logic here


    screen.fill((255, 255, 255))
    draw_grid(None)  #Logic here maybe
    pygame.display.flip()
    clock.tick(60)

pygame.quit()