

def create_matrix(size):
    pass

def place_mines(num):
    pass

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