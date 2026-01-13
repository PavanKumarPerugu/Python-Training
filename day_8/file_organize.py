import os
import shutil

# Folder to organize
folder_path = input("Enter folder path to organize: ")

file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"]
}

# Create folders if not exist
for folder in file_types:
    os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

os.makedirs(os.path.join(folder_path, "Others"), exist_ok=True)

# Organize files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        moved = False
        for folder, extensions in file_types.items():
            if file.lower().endswith(tuple(extensions)):
                shutil.move(
                    file_path,
                    os.path.join(folder_path, folder, file)
                )
                moved = True
                break

        if not moved:
            shutil.move(
                file_path,
                os.path.join(folder_path, "Others", file)
            )

print("Files organized successfully!")
