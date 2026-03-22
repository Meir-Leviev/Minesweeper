import random

def create_matrix(size)->list[list]:
    return [['' for _ in range(size)] for _ in range(size)]

def place_mines(matrix, num_mines):
    rows = len(matrix)
    cols = len(matrix[0])
    total_cells = rows * cols

    if num_mines >= total_cells:
        num_mines = total_cells - 1

    mines_placed = 0
    while mines_placed < num_mines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)

        if matrix[r][c] != "M":
            matrix[r][c] = "M"
            mines_placed += 1

    return matrix


def numbers():
    pass

def cover_matrix():
    pass

def flag_mine():
    pass

def player_action():
    pass

def check_square():
    pass

def stepped_on_a_mine():
    pass

def check_flags():
    pass

def win_game():
    pass

def lose_game():
    pass