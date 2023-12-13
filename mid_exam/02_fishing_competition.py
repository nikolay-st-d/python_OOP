n = int(input())
fishing_area = []
ship_position = ()
quota = 20
catch = 0
whirlpool = False
for row_index in range(n):
    row = list(input())
    if 'S' in row:
        ship_position = (row_index, row.index('S'))
    fishing_area.append(row)


while True:
    command = input()
    next_row = 0
    next_col = 0
    current_row, current_col = ship_position
    if command == 'collect the nets':
        break
    elif command == 'up':
        next_row = ship_position[0] - 1
        next_col = ship_position[1]
    elif command == 'down':
        next_row = ship_position[0] + 1
        next_col = ship_position[1]
    elif command == 'left':
        next_row = ship_position[0]
        next_col = ship_position[1] - 1
    elif command == 'right':
        next_row = ship_position[0]
        next_col = ship_position[1] + 1

    if next_row == n:
        next_row = 0
    if next_row < 0:
        next_row = n - 1
    if next_col == n:
        next_col = 0
    if next_col < 0:
        next_col = n - 1

    if fishing_area[next_row][next_col].isnumeric():
        catch += int(fishing_area[next_row][next_col])
    elif fishing_area[next_row][next_col] == 'W':
        print(f'You fell into a whirlpool! The ship sank and you lost the fish you caught. '
              f'Last coordinates of the ship: [{next_row},{next_col}]')
        whirlpool = True
        break
    ship_position = (next_row, next_col)
    fishing_area[current_row][current_col] = '-'
    fishing_area[next_row][next_col] = 'S'

if not whirlpool:
    if catch >= quota:
        print('Success! You managed to reach the quota!')
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {quota - catch} tons of fish more.")
    if catch > 0:
        print(f'Amount of fish caught: {catch} tons.')
    [print(''.join(row)) for row in fishing_area]
