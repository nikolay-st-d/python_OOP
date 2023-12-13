def extract_submatrix(matrix, start_row, start_col, submatrix_width, submatrix_height):
    if (
        start_row < 0
        or start_col < 0
        or start_row + submatrix_height > len(matrix)
        or start_col + submatrix_width > len(matrix[0])
    ):
        raise ValueError("Indices are out of bounds")
    submatrix = []
    for i in range(start_row, start_row + submatrix_height):
        subrow = []
        for j in range(start_col, start_col + submatrix_width):
            subrow.append(matrix[i][j])
        submatrix.append(subrow)
    return submatrix


def print_matrix(some_matrix):
    for current_row in some_matrix:
        print(*current_row)


def matrix_sum(some_matrix):
    """ Matrix shall contain INT elements only """
    sum_of_matrix = 0
    for current_row in some_matrix:
        sum_of_matrix += sum(current_row)
    return sum_of_matrix

