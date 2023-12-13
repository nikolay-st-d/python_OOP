chars_to_replace = ["-", ",", ".", "!", "?"]
file = open('text.txt', 'r')
lines = file.readlines()
final_line = []
for line_num, line in enumerate(lines):
    if line_num % 2 == 0:
        new_line = line.strip()
        for char in chars_to_replace:
            new_line = new_line.replace(char, '@')
            final_line = new_line.split(' ')
        print(*reversed(final_line))
file.close()