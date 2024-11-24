import os

# Automatically determine the base directory where the script is located
base_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
output_directory = os.path.join(base_directory, "docs")
output_file_name = os.path.join(output_directory, "formflow-automation_XML.xml")

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# File extensions to include
dev_file_extensions = {
    ".cs", ".json", ".xml", ".html", ".js", ".css", ".ts",
    ".py", ".java", ".cpp", ".c", ".h", ".go", ".rb", ".php",
    ".sh", ".sql", ".yml", ".yaml", ".md", ".txt", ".toml", ".env"
}

# Traverse all files in the project directory, skipping the "venv" folder
filtered_files = []
for root, dirs, files in os.walk(base_directory):
    # Exclude the "venv" directory
    dirs[:] = [d for d in dirs if d != "venv"]
    for file in files:
        if os.path.splitext(file)[1] in dev_file_extensions:
            relative_path = os.path.relpath(os.path.join(root, file), base_directory)
            filtered_files.append(relative_path)

# Create XML structure for filtered files
xml_output = '<documents>\n'

for index, file in enumerate(filtered_files, start=1):
    full_path = os.path.join(base_directory, file)
    with open(full_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    # Escape content for XML safety
    escaped_content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    # Add file to XML structure
    xml_output += f'  <document index="{index}">\n'
    xml_output += f'    <source>{file}</source>\n'
    xml_output += f'    <document_content>\n{escaped_content}\n    </document_content>\n'
    xml_output += f'  </document>\n'

xml_output += '</documents>'

# Save the XML output
with open(output_file_name, 'w', encoding='utf-8') as output_file:
    output_file.write(xml_output)

# Print file location and wait for user input to exit
print(f"\nXML file successfully saved!")
print(f"File Name: formflow-automation_XML.xml")
print(f"Location: {output_file_name}")
input("\nPress any key to exit...")