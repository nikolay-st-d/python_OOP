math_string = list(input())
left_par = []
for index in range(len(math_string)):
    if math_string[index] == '(':
        left_par.append(index)
    elif math_string[index] == ')':
        start_index = left_par.pop()
        match = math_string[start_index:index + 1]
        print(''.join(match))
