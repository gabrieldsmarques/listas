notas = [5, 5, 7, 8, 5, 6, 9, 10, 7, 8, 3, 2, 0, 1, 10]
med = 0
notas2 = []

for i in notas:
    med += i

med = med / len(notas)

for i in notas:
    if i > med:
        notas2.append(i)
    
print(f"As notas que estão acima da média são essas: {notas2}")
