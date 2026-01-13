import os
import csv

# current working directory
print("\ncurrent working directory")
print(os.getcwd())

# Get the folder where the script is
script_dir = os.path.dirname(os.path.abspath(__file__))

# location where the script is
print("\nlocation where the script is")
print(script_dir)

# Build full path to data.txt
file_path = os.path.join(script_dir, "students.csv")
file1_path = os.path.join(script_dir, "employees.csv")
file2_path = os.path.join(script_dir, "marks.csv")
file3_path = os.path.join(script_dir, "users.csv")

#creating a csv file with some content in it
f = open(file_path, "w")
f.write("name,age,city\n")
f.write("Alice,20,Delhi\n")
f.write("Bob,22,Mumbai\n")
f.close()

#creating a csv file with some content in it
with open(file1_path, "w") as f:
    f.write("id,name,salary\n")
    f.write("1,John,50000\n")
    f.write("2,Emma,60000\n")

#creating a csv file with some content in it
with open(file2_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "math", "science"])
    writer.writerow(["Alice", 85, 90])
    writer.writerow(["Bob", 78, 88])

#creating a csv file with some content in it
with open(file3_path, "w", newline="") as f:
    fieldnames = ["username", "email", "age"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({
        "username": "alex",
        "email": "alex@gmail.com",
        "age": 25
    })

#reading a csv file with some content in it
with open(file_path, "r", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#reading a csv file with some content in it
with open(file_path, "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

#appending a new line to a csv file with some content in it
with open(file2_path, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Charlie", 92, 95])

#reading a csv file with some content in it
with open(file2_path, "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

#reading a csv file with some content in it
with open(file2_path, "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        math = int(row["math"])
        science = int(row["science"])
        print(math + science)

#appending a new line to a csv file with some content in it
with open(file2_path, "r+", newline="") as f:
    reader = csv.reader(f)
    data = list(reader)
    data.append(["David", 80, 85])
    f.seek(0)
    writer = csv.writer(f)
    writer.writerows(data)
    reader1 = csv.reader(f)
    for row in reader1:
        print(row)


