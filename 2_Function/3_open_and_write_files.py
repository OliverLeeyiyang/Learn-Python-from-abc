import os

def create_txt_file(filename):
    """Create a .txt file in the current folder if it doesn't exist."""
    if not filename.endswith('.txt'):
        filename += '.txt'
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            pass  # Create the file
    return filename

def write_line_to_file(filename, text):
    """Write the input text into the txt file with a new line."""
    if not filename.endswith('.txt'):
        filename += '.txt'
    with open(filename, 'a') as f:
        f.write(text + '\n')

def print_file_content(filename):
    """Print the content written in the .txt file."""
    if not filename.endswith('.txt'):
        filename += '.txt'
    with open(filename, 'r') as f:
        content = f.read()
        print(content)

# Example usage:
fname = create_txt_file('example')
write_line_to_file(fname, 'Hello, world!')
write_line_to_file(fname, 'Another line.')
print_file_content(fname)
