from functools import reduce


square = lambda n: n * n
print(square(4))

nums = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)

add = lambda a, b: a + b
print(add(3, 7))

nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)

prices = [100, 200, 300]
taxed = list(map(lambda price: price * 1.1, prices))  # add 10% tax
print(taxed)  # [110.0, 220.0, 330.0]


scores = [55, 70, 85, 90]
high_scores = list(filter(lambda s: s > 80, scores))
print(high_scores)  # [85, 90]

employees = [('Alice', 50000), ('Bob', 40000), ('Charlie', 60000)]
sorted_employees = sorted(employees, key=lambda x: x[1])
print(sorted_employees)
# [('Bob', 40000), ('Alice', 50000), ('Charlie', 60000)]

nums = [10, 5, 20, 15]
max_num = reduce(lambda x, y: x if x > y else y, nums)
print(max_num)  # 20

words = ['Hello', 'World', 'Python']
sentence = reduce(lambda x, y: x + ' ' + y, words)
print(sentence)  # "Hello World Python"



