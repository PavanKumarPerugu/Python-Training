'''
3️⃣ List & Dict Comprehensions (Advanced)

✅ Concept:

Comprehensions let you create lists, sets, or dicts in one line — more readable and efficient.

'''

# List comprehension with condition
squares = [x**2 for x in range(10) if x % 2 == 0]

# Nested comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]

# Dictionary comprehension
students = {"John": 85, "Anita": 92, "Ravi": 78}
passed = {name: mark for name, mark in students.items() if mark > 80}

print(squares)
print(matrix)
print(passed)
