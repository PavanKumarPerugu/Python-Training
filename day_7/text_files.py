import os

# current working directory
print("\ncurrent working directory")
print(os.getcwd())

# Get the folder where the script is
script_dir = os.path.dirname(os.path.abspath(__file__))

# location where the script is
print("\nlocation where the script is")
print(script_dir)

# Build full path to data.txt
file_path = os.path.join(script_dir, "data.txt")

file = open(file_path, "r")  # read
print("\n"+ file.read())
file.close()

with open(file_path, "r") as file:
    content = file.read()
    print("\n"+ content)

with open(file_path, "r") as f: #prints a single line at a time
  print("\n"+f.readline())
  print(f.readline())

with open(file_path, "r") as f: #prints line by line but for all
  for x in f:
    print(x)

with open(file_path, "a") as f:
  f.write("\nNow the file has more content!")

#open and read the file after the appending:
with open(file_path, "r") as f:
  print(f.read())


line_to_remove = 5  # line number (1-based)
with open(file_path, "r") as file:
    lines = file.readlines()
with open(file_path, "w") as file:
    for i, line in enumerate(lines, start=1):
        if i != line_to_remove:
            file.write(line)

#deleting a file
if os.path.exists(os.path.join(script_dir, "myfile.txt")):
  os.remove(os.path.join(script_dir, "myfile.txt"))
else:
  print("The file does not exist")

#creating a file
f = open(os.path.join(script_dir, "myfile.txt"), "x")


file = open("data.txt", "r") #since the current worrking directory and the directory for the script files are different
print("\n"+ file.read())
file.close()

with open("data.txt", "r") as file:
    content = file.read()
    print("\n"+ content)