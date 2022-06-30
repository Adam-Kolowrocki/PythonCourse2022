import os


def user_filename():
    filename = input(f'Type a name of file to open ->')
    return filename


def open_file(filename):
    if not os.path.isfile(filename):
        print(f'There is no such a fie "{filename}".')
    elif os.stat(filename) == 0:
        print(f'File "{filename}" is empty.')
    else:
        with open(filename, 'r') as f:
            file = f.read()
        return file


def write_file(filename, content):
    if os.path.exists(filename) and os.stat(filename).st_size > 0:
        print("File exist and it's not empty")
    else:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'File {filename} is saved!')
