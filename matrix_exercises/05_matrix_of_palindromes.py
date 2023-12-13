import string
from collections import deque

letters = deque(list(string.ascii_lowercase))


def print_matrix_int(some_matrix):
    for current_row in some_matrix:
        print(*current_row)


rows, columns = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    curr_row = []
    for column in range(columns):
        start_letter = letters[row]
        letters.rotate(-row)
        mid_letter = letters[column]
        letters.rotate(row)
        curr_row.append(start_letter + mid_letter + start_letter)
    matrix.append(curr_row)
print_matrix_int(matrix)

