def write_file(file_name, file_content):
    """Function to write content to a file."""
    with open(f'{file_name}.txt', 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """Function to append content to a file."""
    with open(f'{file_name}.txt', 'a') as file:
        file.write(append_content)

def read_file(file_name):
    """Function to read content from a file."""
    with open(f'{file_name}.txt', 'r') as file:
        return file.read()
