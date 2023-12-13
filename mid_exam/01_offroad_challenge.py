from collections import deque

fuel_qty = [int(x) for x in input().split()]
consumption_index = deque([int(x) for x in input().split()])
quantities = deque([int(x) for x in input().split()])
number_of_altitudes = len(fuel_qty)
altitudes_count = 0
reached_altitudes = 0
while fuel_qty:
    result = fuel_qty.pop() - consumption_index.popleft()
    quantity_needed = quantities.popleft()
    altitudes_count += 1
    if result < quantity_needed:
        print(f"John did not reach: Altitude {altitudes_count}")
        break
    else:
        print(f"John has reached: Altitude {altitudes_count}")
        reached_altitudes += 1

if number_of_altitudes > reached_altitudes > 0:
    print('John failed to reach the top.')
    print('Reached altitudes:', end=' ')
    reached_alts = []
    for i in range(reached_altitudes):
        reached_alts.append(f'Altitude {i + 1}')
    print(', '.join(reached_alts))
if reached_altitudes == 0:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")
if reached_altitudes == number_of_altitudes:
    print("John has reached all the altitudes and managed to reach the top!")
