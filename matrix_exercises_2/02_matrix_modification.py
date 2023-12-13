rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
while True:
    input_data = input().split()
    if input_data[0] == 'END':
        break
    command = input_data[0]
    r, c, value = [int(x) for x in input_data[1:]]
    columns = len(matrix[0])
    if r < 0 or r >= rows or c < 0 or c >= columns:
        print('Invalid coordinates')
        continue
    else:
        if command == 'Add':
            matrix[r][c] += value
        elif command == 'Subtract':
            matrix[r][c] -= value

[print(*row) for row in matrix]
