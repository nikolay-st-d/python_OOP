from collections import deque

number_of_pumps = int(input())
pumps_input = deque()
for _ in range(number_of_pumps):
    pumps_input.append([int(x) for x in input().split()])

total_distance = 0
for i in range(len(pumps_input)):
    total_distance += pumps_input[i][1]
fuel_left = 0
current_distance = 0
pumps = deque([x for x in pumps_input])

while current_distance < total_distance:
    fuel, distance = pumps[0]
    if fuel + fuel_left >= distance:
        fuel_left += fuel - distance
        current_distance += distance
    pumps.rotate(-1)
print(pumps_input.index(pumps[0]))


# debug
print(total_distance)
print(current_distance)
print(pumps_input)
print(pumps)
