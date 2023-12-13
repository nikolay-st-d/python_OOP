n = int(input())
matrix = [list(input()) for _ in range(n)]

moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

max_hits = float('-inf')
position_max_hits = []

