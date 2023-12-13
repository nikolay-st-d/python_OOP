n = int(input())
stack = []
for _ in range(n):
    data = input().split()
    command = data[0]
    if command == '1':
        stack.append(int(data[1]))
    elif command == '2' and stack:
        stack.pop()
    elif command == '3' and stack:
        print(max(stack))
    elif command == '4' and stack:
        print(min(stack))
stack_as_str = [str(x) for x in stack]
print(', '.join(reversed(stack_as_str)))

