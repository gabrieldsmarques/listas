numbers = [(2, 8), (4, 5, 6), (1, 2)]

med = map(lambda numbers: sum(numbers) / len(numbers), numbers)

filtered = filter(lambda x: x > 5, med)

print(list(filtered))