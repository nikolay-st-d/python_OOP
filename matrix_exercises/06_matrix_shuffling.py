def valid_indexes(r1, c1, r2, c2, r, c):
    if 0 <= r1 < r and 0 <= r2 < r and 0 <= c1 < c and 0 <= c1 < c:
        return True
    return False


rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]

input_data = input()
while input_data != 'END':
    raw_command = input_data.split()
    if len(raw_command) == 5 and raw_command[0] == 'swap':
        row_1, col_1, row_2, col_2 = [int(x) for x in raw_command[1:]]
        if valid_indexes(row_1, col_1, row_2, col_2, rows, cols):
            matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
            [print(*row) for row in matrix]
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
    input_data = input()
