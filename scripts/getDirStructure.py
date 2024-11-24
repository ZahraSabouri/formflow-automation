import os

def directory_structure(path, level=0, skip_dirs=None):
    """
    This function builds a string containing the directory structure of a given path.

    Args:
        path: The path to the directory for which you want to see the structure.
        level: The current level of indentation (default=0).
        skip_dirs: A list of directory names to exclude (default=None).

    Returns:
        A string containing the directory structure.
    """
    if skip_dirs is None:
        skip_dirs = []

    indent = '│  ' * level
    text = f'{indent}├── {os.path.basename(path)}/'  # Build the string

    items = os.listdir(path)
    for i, item in enumerate(items):
        # Process current item
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path) and item not in skip_dirs:
            text += f'\n{directory_structure(item_path, level + 1, skip_dirs)}'
        elif os.path.isfile(item_path):
            if i == len(items) - 1:
                text += f'\n{indent}└── {item}'
            else:
                text += f'\n{indent}│── {item}'

    return text

# Automatically determine the base directory where the script is located
base_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
output_directory = os.path.join(base_directory, "docs")
output_file_name = os.path.join(output_directory, "formflow-automation.layout.md")

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Directories to exclude
skip_dirs = ['.git', '__pycache__', 'venv', 'bin', 'obj', 'lib', 'dist']

# Generate the directory structure
directory_text = directory_structure(base_directory, skip_dirs=skip_dirs)

# Write the text to the output file
with open(output_file_name, 'w', encoding='utf-8') as f:
    f.write(directory_text)

# Print file location and wait for user input to exit
print(f"\nDirectory structure successfully saved!")
print(f"File Name: formflow-automation.layout.md")
print(f"Location: {output_file_name}")
input("\nPress any key to exit...")
