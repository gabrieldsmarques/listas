from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
rnumbers = reduce(lambda x, y: x + y, numbers)
print(rnumbers)