import os


def read_py_files(directory, exclude_dirs):
    py_files_content = []
    for root, dirs, files in os.walk(directory):
        # Remove the excluded directories from the walk
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        py_files_content.append((file_path, content))
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    return py_files_content


def save_to_file(py_files_content, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for file_path, content in py_files_content:
            f.write(f"File: {file_path}\n")
            f.write(content)
            f.write("\n" + "-" * 80 + "\n\n")


if __name__ == "__main__":
    # Specify the directories to exclude
    exclude_dirs = ['.venv', '.idea']
    # Get all Python files and their content
    py_files_content = read_py_files('.', exclude_dirs)
    # Save to a file
    save_to_file(py_files_content, "python_files_output.txt")
    print("Python files have been saved to python_files_output.txt")
