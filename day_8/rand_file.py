import os
import random
import string

import os

# current working directory
print("\ncurrent working directory")
print(os.getcwd())

# Get the folder where the script is
script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)

# going one folder up
script_dir = os.path.dirname(script_dir)
print(script_dir)

os.chdir(script_dir)


# -------------------------------
# Folder setup
# -------------------------------
folder_name = "dummy_files_100"
os.makedirs(folder_name, exist_ok=True)

# -------------------------------
# File types and extensions
# -------------------------------
file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".txt", ".docx", ".pptx"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Archives": [".zip", ".rar"],
    "Scripts": [".py", ".js", ".html"]
}

# Flatten all extensions for random generation
all_extensions = [ext for exts in file_types.values() for ext in exts]

# -------------------------------
# Function to generate random filename
# -------------------------------
def random_filename(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# -------------------------------
# Generate 100+ dummy files
# -------------------------------
num_files = 120  # adjust as needed

for _ in range(num_files):
    filename = random_filename()
    ext = random.choice(all_extensions)
    file_path = os.path.join(folder_name, filename + ext)
    
    # Write minimal content depending on type
    with open(file_path, "w") as f:
        if ext in [".txt", ".py", ".js", ".html"]:
            f.write(f"This is a dummy {ext} file named {filename}{ext}")
        elif ext in [".pdf", ".docx", ".pptx"]:
            f.write("Dummy document content")
        elif ext in [".mp3", ".wav"]:
            f.write("Dummy music file content")
        elif ext in [".mp4", ".mkv", ".avi"]:
            f.write("Dummy video file content")
        elif ext in [".jpg", ".jpeg", ".png", ".gif"]:
            f.write("Dummy image file content")
        else:
            f.write("Dummy file content")

print(f"Generated {num_files} dummy files in folder '{folder_name}'")
