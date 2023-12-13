import os


def create_file(args_):
    file_name = args_[0]
    with open(file_name, 'w'):
        pass


def add_content(args_):
    file_name, content = args_
    with open(file_name, 'a') as file:
        file.write(f'{content}\n')


def replace_string(args_):
    file_name, old_str, new_str = args_
    new_lines = []
    try:
        with open(file_name, 'r') as file:
            content = file.readlines()
            for line in content:
                new_line = line.replace(old_str, new_str)
                new_lines.append(new_line)
        with open(file_name, 'w') as file:
            for line in new_lines:
                file.write(line)
    except FileNotFoundError:
        print('An error occurred')


def delete_file(args_):
    file_name = args_[0]
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print('An error occurred')


while True:
    input_line = input()
    if input_line == 'End':
        break
    command, *args = input_line.split('-')
    if command == 'Create':
        create_file(args)
    elif command == 'Add':
        add_content(args)
    elif command == 'Replace':
        replace_string(args)
    elif command == 'Delete':
        delete_file(args)
