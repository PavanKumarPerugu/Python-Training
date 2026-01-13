#1. finding smallest and largest numbers in a list
print("\nLargest and Smallest numbers in a given list: ")
nums = [5, 2, 9, 1, 7]
largest = nums[0]
smallest = nums[0]
for n in nums:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
print("Largest:", largest)
print("Smallest:", smallest)

#2. removing duplicates from a list
print("\nRemoving duplicates from a given list: ")
nums = [1, 2, 2, 3, 4, 4]
unique = []
for n in nums:
    if n not in unique:
        unique.append(n)
print(unique)

#3. sorting without using sort function
print("\nSorting without using sort function: ")
nums = [4, 1, 3, 2]
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
print(nums)


#4. Converting tuple to list
print("\nConverting tuple to a list: ")
t = (1, 2, 3)
lst = list(t)
print(lst)

#5. finding length of a tuple
print("\nFinding length of a tuple: ")
t = (10, 20, 30)
print("Length:", len(t))

#6. checking if an element exist in tuple
print("\nChecking if an element a tuple: ")
t = (1, 2, 3)
x = 2
if x in t:
    print("Found")
else:
    print("Not Found")

#7. counting frequency of letters in a word
print("\nCounting frequency of letters in a word: ")
s = "python"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)


#8. finding key with maximum value
print("\nFinding key with maximum value: ")
marks = {"A": 85, "B": 92, "C": 78}
max_key = max(marks, key=marks.get)
print("Topper:", max_key)


#9. union and intersection of sets
print("\nUnion and Intersection of Sets: ")
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)
print("Intersection:", a & b)

#9. removing duplicates from a list using sets
print("\nRemoving duplicates from a list using sets: ")
nums = [1, 2, 2, 3, 3]
unique = list(set(nums))
print(unique)

#10. create dictionary of numbers and cubes
print("\nCreate dictionary of numbers and cubes: ")
cubes = {x: x**3 for x in range(1, 6)}
print(cubes)
