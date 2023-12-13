from collections import deque
water_quantity = int(input())
queue = deque()

name = input()
while name != 'Start':
    queue.append(name)
    name = input()

command = input()
while command != 'End':
    if len(command.split(' ')) == 1:
        water_outgo = int(command.split(' ')[0])
        if water_quantity >= water_outgo:
            print(f'{queue.popleft()} got water')
            water_quantity -= water_outgo
        else:
            print(f'{queue.popleft()} must wait')
    else:
        water_refill = int(command.split(' ')[1])
        water_quantity += water_refill
    command = input()
print(f'{water_quantity} liters left')