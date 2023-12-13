from collections import deque

clothes = deque([int(x) for x in input().split()])
rack_capacity = int(input())
racks_counter = 1
current_rack = 0
while clothes:
    if current_rack + clothes[-1] <= rack_capacity:
        current_rack += clothes.pop()
    else:
        racks_counter += 1
        current_rack = 0
print(racks_counter)
