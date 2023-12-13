n = int(input())
# matrix = []
# for i in range(n):
#     matrix.append([int(x) for x in input().split(', ')])
matrix = [[int(x) for x in input().split(', ')] for _ in range(n) ]
primary_diagonal = []
for i in range(len(matrix)):
    primary_diagonal.append(matrix[i][i])
print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
secondary_diagonal = []
for i in range(len(matrix)):
    secondary_diagonal.append(matrix[i][len(matrix[0]) - 1 - i])
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")

