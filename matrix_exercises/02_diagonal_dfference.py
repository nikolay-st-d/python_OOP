n = int(input())
matrix = [[] for _ in range(n)]
# for _ in range(n):
#     matrix.append([])

for row_index in range(n):
    column = [int(x) for x in input().split()]
    for col_index in range(n):
        matrix[col_index].append(column[col_index])

primary_diagonal = []
for i in range(len(matrix)):
    primary_diagonal.append(matrix[i][i])
secondary_diagonal = []
for i in range(len(matrix)):
    secondary_diagonal.append(matrix[i][len(matrix[0]) - 1 - i])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
