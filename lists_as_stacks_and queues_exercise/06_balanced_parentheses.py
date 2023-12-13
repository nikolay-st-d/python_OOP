# NOT RESOLVED

from collections import deque

roundy = ')'
boxy = ']'
curly = '}'
sequence = deque(list(input()))
balanced = False

while sequence:
    first = sequence[0]
    second = sequence[1]
    if ((first == '(' and second == ')')
            or (first == '[' and second == ']')
            or (first == '{' and second == '}')):
        balanced = True
        sequence.popleft()
        sequence.popleft()
    else:
        sequence.rotate(-1)
    if len(sequence) == 1:
        balanced = False
        break
if balanced:
    print('YES')
else:
    print('NO')
