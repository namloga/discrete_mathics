def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def write_file(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)