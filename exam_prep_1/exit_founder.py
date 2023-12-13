first_player, second_player = input().split(', ')
maze = []
for _ in range(6):
    maze.append([x for x in input().split()])
moves_counter = -1
rests = {first_player: False, second_player: False}

while True:
    moves_counter += 1
    command_line = input()

    if moves_counter % 2 == 0:
        player = first_player
    else:
        player = second_player
    if rests[player]:
        rests[player] = False
        continue

    row = int(command_line[1])
    col = int(command_line[-2])

    if maze[row][col] == 'E':
        print(f'{player} found the Exit and wins the game!')
        break
    elif maze[row][col] == 'T':
        winner = first_player
        if player == first_player:
            winner = second_player
        print(f'{player} is out of the game! The winner is {winner}.')
        break
    elif maze[row][col] == 'W':
        rests[player] = True
        print(f'{player} hits a wall and needs to rest.')
