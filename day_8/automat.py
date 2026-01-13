import os

# current working directory
print("\ncurrent working directory")
print(os.getcwd())

# Get the folder where the script is
script_dir = os.path.dirname(os.path.abspath(__file__))

# going one folder up
script_dir = os.path.dirname(script_dir)

#changin the current working directory to new
os.chdir(script_dir)

# location where the python is working
print("\nlocation where the script is")
print(script_dir)

#creating the directories / creating the folders
folders = ["Images", "Docs", "Videos"]
for folder in folders:
    os.makedirs(script_dir+"/dummy_day/"+folder, exist_ok=True)

#making sure to change the current working directory ro dummy_day folder
os.chdir(script_dir+"/dummy_day/")

#changing the names of the files and folders exist in the current working directory by listing and enumerating them in a loop
for i, file in enumerate(os.listdir()):
    os.rename(file, f"file_{i}.txt")

#changing the files or folders names back to their original ones
for i, file in enumerate(os.listdir()):
    os.rename(file, folders[i])

