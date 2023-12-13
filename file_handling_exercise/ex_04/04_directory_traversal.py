import os

files = {}
# dir_to_scan = input('DIR to scan: ')  # Input 'test_dir' or '.' or '..'
dir_to_scan = 'test_dir'
CURRENT_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(CURRENT_DIRECTORY_PATH, dir_to_scan)
dir_content = os.listdir(path)

for file in dir_content:
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        ext = file.split('.')[-1]
        if ext not in files.keys():
            files[ext] = []
        files[ext].append(file)

for key, values in sorted(files.items()):
    print(f'.{key}')
    for file_name in values:
        print(f'- - - {file_name}')
