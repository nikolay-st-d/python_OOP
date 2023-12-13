from collections import deque
rows, columns = [int(x) for x in input().split()]
letters = deque(x for x in input())
matrix = []

for row in range(rows):
    new_row = deque()
    for col in range(columns):
        if row % 2 == 0:
            new_row.append(letters[0])
            letters.rotate(-1)
        else:
            new_row.appendleft(letters[0])
            letters.rotate(-1)
    matrix.append([x for x in new_row])

for row in matrix:
    print(*row, sep='')