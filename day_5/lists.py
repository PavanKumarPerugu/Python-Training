#1. creating a tuple
print("\nCreating a tuple: ")
nums = [10, 20, 30, 40]
nums.append(50)
nums.remove(20)
nums[0] = 100
print(nums)

#2. creating a tuple
print("\nCreating a tuple: ")
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#3. reading from a tuple
print("\nReading from a tuple: ")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#4. reading from a tuple
print("\nReading from a tuple: ")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#5. checking for an element in a tuple
print("\nChecking for an element in a tuple: ")
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#6. printing all the elements in a tuple
print("\nPrinting all the elements in a tuple: ")
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#7. list comprehension
print("\nList comprehension: ")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#8. reverse ordering a list
print("\nReverse ordering a list: ")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#9. copying a list
print("\nCopying a list: ")
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#10. copying a list
print("\nCopying a list: ")
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#11. sorting a list using own function
print("\nSorting a list using own function: ")
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#12. concatination of two lists
print("\nConcatination of 2 lists: ")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)