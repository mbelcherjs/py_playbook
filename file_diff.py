import difflib
import sys

def show_diff(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()

        diff = difflib.unified_diff(
            file1_lines, file2_lines,
            fromfile=file1_path,
            tofile=file2_path,
            lineterm=''
        )

        for line in diff:
            print(line)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff_files.py file1.txt file2.txt")
        sys.exit(1)

    show_diff(sys.argv[1], sys.argv[2])
