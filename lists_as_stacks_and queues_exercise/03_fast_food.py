from collections import deque
sandwiches = int(input())
orders = deque([int(x) for x in input().split()])
print(max(orders))
# print(orders)
for _ in range(len(orders)):
    if orders[0] <= sandwiches:
        order = orders.popleft()
        sandwiches -= order
if orders:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")
else:
    print('Orders complete')
