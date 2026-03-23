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


def place_numbers(mat_with_mines):
    rows = len(mat_with_mines)
    columns = len(mat_with_mines[0])
    for r in range(rows):
        for c in range(columns):
            if mat_with_mines[r][c] == "M":
                continue
            mine_cnt = 0

            for i in range(max(0, r - 1), min(rows, r + 2)):
                for j in range(max(0, c - 1), min(columns, c + 2)):
                    if mat_with_mines[i][j] == "M":
                        mine_cnt += 1

            if mine_cnt > 0:
                mat_with_mines[r][c] = str(mine_cnt)
    return mat_with_mines

def save_score():
    pass

def open_empty_blocks():
    pass

def create_board(level):
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