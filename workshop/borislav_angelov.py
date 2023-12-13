ROWS = 6
COLS = 7
WINNER_LENGTH = 4


class FullColumnError(Exception):
    pass


def print_matrix(matrix):
    for row in matrix:
        print(row)


def is_valid_column_choice(selected_column_index):
    return 0 <= selected_column_index < COLS


def place_player_number(column_index, matrix, player_number):
    for row_index in range(ROWS - 1, -1, -1):
        if matrix[row_index][column_index] == 0:
            matrix[row_index][column_index] = player_number
            return row_index, column_index
    else:
        raise FullColumnError


def is_valid_place(row, col):
    return 0 <= row < ROWS and 0 <= col < COLS


def is_winner(matrix, row, col, player):
    begin = col - WINNER_LENGTH if col - WINNER_LENGTH > 0 else 0
    subrow, subcol, left_diagonal, right_diagonal = matrix[row][begin:col + WINNER_LENGTH], [], [], []

    for current_row in range(row - WINNER_LENGTH, row + WINNER_LENGTH):
        if is_valid_place(current_row, col):
            subcol.append(matrix[current_row][col])
        if is_valid_place(current_row, col - row + current_row):
            left_diagonal.append(matrix[current_row][col - row + current_row])
        if is_valid_place(current_row, col + row - current_row):
            right_diagonal.append(matrix[current_row][col + row - current_row])

    return any(str(player) * WINNER_LENGTH in ''.join(map(str, lis)) for lis in
               (subrow, subcol, left_diagonal, right_diagonal))


matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]
print_matrix(matrix)

player = 1
while True:
    try:
        selected_column_number = int(input(f"Player {player}, please choose a column: "))
        selected_column_index = selected_column_number - 1
        if not is_valid_column_choice(selected_column_index):
            raise ValueError
        current_row, current_col = place_player_number(selected_column_index, matrix, player)
        if is_winner(matrix, current_row, current_col, player):
            print(f"Player {player} wins!")
            print_matrix(matrix)
            break
        print_matrix(matrix)
    except ValueError:
        print(f"Player {player}, please select number between 1 and {COLS}")
        continue
    except FullColumnError:
        print(f"Player {player}, this column is full, please select another one")
        continue

    player += 1
    player = 2 if player % 2 == 0 else 1