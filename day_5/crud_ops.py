#1. creating a list
print("\nCreating a list: ")
nums = []
nums = [1, 2, 3, 4]
print(nums)

#2. reading from a list
print("\nReading from a list: ")
nums = [10, 20, 30, 40]
for n in nums:
    print(n)
print(nums[0])  
print(nums[-1]) 

#3. updating a list
print("\nUpdating a list: ")
nums = [10, 20, 30, 40]
nums[1] = 25
print(nums) 
nums[2:] = [35, 45]
print(nums)  

#4. deleting list elements
print("\nDeleting list elements: ")
nums = [10, 20, 30, 40]
del nums[1]
print(nums)  
nums.remove(30)
print(nums)  
nums.pop()
print(nums)

#5. creating a dictionary
print("\nCreating a dictionary: ")
student = {}
student = {"name": "Alex", "age": 15, "grade": "A"}
print(student)

#6. reading from a dictionary
print("\nReading from a dictionary: ")
print(student["name"])
print(student.keys())
print(student.values())
print(student.items())

#7. updating a dictionary
print("\nUpdating a dictionary: ")
student["age"] = 16
student["city"] = "Delhi"
print(student)

#8. deleting dictionary elements
print("\nDeleting dictionary elements: ")
del student["grade"]
student.pop("city", None)
print(student)
