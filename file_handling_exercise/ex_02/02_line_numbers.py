import string

punctuation_marks = string.punctuation

with open('text.txt') as text_file, open('output.txt', 'a') as output_file:
    lines = text_file.readlines()

    for line_num, line in enumerate(lines):
        line = line.strip()
        char_count = 0
        punctuation_count = 0
        for char in line:
            if char.isalpha():
                char_count += 1
            elif char in punctuation_marks:
                punctuation_count += 1

        output_file.write(f"Line {line_num + 1}: {line} ({char_count})({punctuation_count})\n")
