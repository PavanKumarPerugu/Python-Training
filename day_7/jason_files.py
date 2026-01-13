import os
import json

# File path
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "students.json")

# Step 1: Create initial dictionary of students
students = {
    "Bob": {"name": "Bob", "math": 78, "science": 88}
}

with open(file_path, "w") as f:
    json.dump(students, f, indent=4)

# Step 2: Read JSON
with open(file_path, "r") as f:
    data = json.load(f)
print("\nOriginal data:")
print(data)

# Step 3: Add a new student
data["David"] = {"name": "David", "math": 80, "science": 85}

# Step 4: Write back
with open(file_path, "w") as f:
    json.dump(data, f, indent=4)

# Step 5: Verify
with open(file_path, "r") as f:
    data = json.load(f)
print("\nAfter adding David:")
print(data)




# updating the existing keys Bob and David with incrementing numbers
with open(file_path, "r") as f:
    data = json.load(f)

print("\nOriginal data:")
print(data)

# Step 2: Update keys to numeric keys
new_data = {}
for i, (old_key, value) in enumerate(data.items(), start=1):
    new_key = str(i)   # "1", "2", ...
    new_data[new_key] = value

# Step 3: Write back the updated dictionary
with open(file_path, "w") as f:
    json.dump(new_data, f, indent=4)

# Step 4: Verify
with open(file_path, "r") as f:
    data = json.load(f)

print("\nUpdated numeric keys:")
print(data)


#type conversions from python to json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#type conversions from python to json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
