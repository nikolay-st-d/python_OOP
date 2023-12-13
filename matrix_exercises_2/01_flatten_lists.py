matrix = [[x for x in r.split() if x != ' '] for r in input().split('|')]
for row in reversed(matrix):
    if row:
        print(*row, end=' ')
