'''
4️⃣ Iterators & Generators (Intro)

✅ Concept:

Iterator: An object that can be iterated using next().

Generator: A function that yields items one at a time (memory efficient).

'''

nums = [1, 2, 3]
it = iter(nums)
print(next(it))
print(next(it))
print(next(it))



def countdown(n):
    while n > 0:
        yield n
        n -= 1
for val in countdown(5):
    print(val)