import os

# 1. Get current working directory
print("Current directory:", os.getcwd())
original_dir = os.getcwd()  # <-- fixed here

# 2. Change directory
os.chdir("C:/Users")  # Change to any valid folder
print("After changing directory:", os.getcwd())

# 3. Folder where the script is
script_dir = os.path.dirname(os.path.abspath(__file__))
print("Script directory:", script_dir)

# 4. Build full path to a file
file_path = os.path.join(script_dir, "students.json")
print("File path:", file_path)

# 5. Check if file exists
if os.path.exists(file_path):
    print("File exists")
else:
    print("File does not exist")

# 6. List all files in script directory
print("Files here:", os.listdir(script_dir))

# 7. Change directory back to the original
os.chdir(original_dir)
print("After changing back to original directory:", os.getcwd())
