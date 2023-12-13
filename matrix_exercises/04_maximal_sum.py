def extract_submatrix(my_matrix, start_row, start_col, submatrix_width, submatrix_height):
    if (
            start_row < 0
            or start_col < 0
            or start_row + submatrix_height > len(my_matrix)
            or start_col + submatrix_width > len(my_matrix[0])
    ):
        raise ValueError("Indices out of matrix!")
    sub_matrix = []
    for i in range(start_row, start_row + submatrix_height):
        sub_row = []
        for j in range(start_col, start_col + submatrix_width):
            sub_row.append(my_matrix[i][j])
        sub_matrix.append(sub_row)
    return sub_matrix


def matrix_sum(some_matrix):
    sum_of_matrix = 0
    for current_row in some_matrix:
        sum_of_matrix += sum(current_row)
    return sum_of_matrix


rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
max_sum = float('-inf')
max_matrix = []
for row in range(rows - 2):
    for column in range(columns - 2):
        submatrix = extract_submatrix(matrix, row, column, 3, 3)
        current_sum = matrix_sum(submatrix)
        if current_sum >= max_sum:
            max_sum = current_sum
            max_matrix = submatrix
print(f'Sum = {max_sum}')
for row in max_matrix:
    print(*row)

# alternative print with comprehension
# [print(*row) for row in max_matrix]