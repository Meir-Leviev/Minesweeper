import pygame
from func import *

# For now, I am using fake data for the ui
WIDTH, HEIGHT = 400, 400
TILE_SIZE = 40
ROWS, COLS = 10, 10

NUMBER_COLORS = {
    "1": (0, 0, 255),      # כחול
    "2": (0, 128, 0),    # ירוק
    "3": (255, 0, 0),    # אדום
    "4": (0, 0, 128),    # כחול כהה
    "5": (128, 0, 0),    # חום/אדום כהה
    "6": (0, 128, 128),  # טורקיז
    "7": (0, 0, 0),      # שחור
    "8": (128, 128, 128) # אפור
}

pygame.init()
font = pygame.font.SysFont("Arial", 32)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def draw_grid(game_mat, revealed_mat):
    for r in range(ROWS):
        for c in range(COLS):
            rect = pygame.Rect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE)

            if revealed_mat[r][c]:

                pygame.draw.rect(screen, (200, 200, 200), rect, 1)
#             grate logic here
                content = str(game_matrix[r][c])

                if content == "M":
                    content = ''
                    screen.blit(MINE_IMG, rect)

                if content != "" and content != "0":
                    color = NUMBER_COLORS.get(content, (0, 0, 0))
                    text_surface = font.render(content, True, color)
                    text_rect = text_surface.get_rect(center=rect.center)
                    screen.blit(text_surface, text_rect)

                if content == "" or content == "0":
                    for i in range(max(0, r - 1), min(ROWS, r + 2)):
                        for j in range(max(0, c - 1), min(COLS, c + 2)):
                            if game_mat[i][j] == "" or game_mat[i][j] == 0:
                                revealed_mat[i][j] = True



            else:
#                 A covered square
                pygame.draw.rect(screen, (150, 150, 150), rect)

            # The outline
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)



game_matrix = create_matrix(ROWS)
place_mines(game_matrix, 5)
place_numbers(game_matrix)

# A matrix that will follow what is revealed
revealed_matrix = [[False for _ in range(COLS)] for _ in range(ROWS)]
# --- הוסף את זה אחרי ה-pygame.init() ---
MINE_IMG = pygame.image.load("mine.png")
MINE_IMG = pygame.transform.scale(MINE_IMG, (TILE_SIZE, TILE_SIZE))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position (click)
            if event.button == 1: # left click
                x, y = event.pos  # event.ops return (x,y)
                row, col = y // TILE_SIZE, x // TILE_SIZE
                if 0 <= row < ROWS and 0 <= col < COLS:
                    revealed_matrix[row][col] = True
            elif event.button == 3:  # Right click
                # Flag
                x, y = event.pos  # event.ops return (x,y)
                row, col = y // TILE_SIZE, x // TILE_SIZE
                if 0 <= row < ROWS and 0 <= col < COLS:
                    revealed_matrix[row][col] = True

    #                 Logic for flagging

    #         some logic here



    screen.fill((255, 255, 255))
    draw_grid(game_matrix, revealed_matrix)  #Logic here maybe
    pygame.display.flip()
    clock.tick(60)

pygame.quit()