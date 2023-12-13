def in_board(matrix_rows, matrix_cols, position):
    row_position, col_position = position
    return 0 <= row_position < matrix_rows and 0 <= col_position < matrix_cols


rows, cols = [int(x) for x in input().split(',')]
matrix = []
mouse = ()
cheese = 0
for row_index in range(rows):
    row = list(input())
    matrix.append(row)
    for col_index in range(cols):
        current_element = row[col_index]
        if current_element == 'M':
            mouse = (row_index, col_index)
        elif current_element == 'C':
            cheese += 1

while True:
    command = input()
    if command == 'danger':
        print("Mouse will come back later!")
        break
    next_position = ()
    if command == 'up':
        next_position = (mouse[0] - 1, mouse[1])
    elif command == 'down':
        next_position = (mouse[0] + 1, mouse[1])
    elif command == 'right':
        next_position = (mouse[0], mouse[1] + 1)
    elif command == "left":
        next_position = (mouse[0], mouse[1] - 1)

    if not in_board(rows, cols, next_position):
        print('No more cheese for tonight!')
        break
    else:
        current_row, current_column = mouse
        next_row, next_column = next_position
        if matrix[next_row][next_column] == '*':
            matrix[current_row][current_column] = '*'
            matrix[next_row][next_column] = 'M'
            mouse = (next_row, next_column)
        elif matrix[next_row][next_column] == 'C':
            matrix[current_row][current_column] = '*'
            matrix[next_row][next_column] = 'M'
            mouse = (next_row, next_column)
            cheese -= 1
            if cheese == 0:
                print('Happy mouse! All the cheese is eaten, good night!')
                break
        elif matrix[next_row][next_column] == 'T':
            matrix[current_row][current_column] = '*'
            matrix[next_row][next_column] = 'M'
            mouse = (next_row, next_column)
            print('Mouse is trapped!')
            break
        elif matrix[next_row][next_column] == '@':
            continue


[print(''.join(row)) for row in matrix]