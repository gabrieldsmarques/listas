nums = [1, 2, 1, 2, 3, 4, 5, 3, 4, 5]
aux = []

for i in nums:
    if i not in aux:
        aux.append(i)

print(aux)