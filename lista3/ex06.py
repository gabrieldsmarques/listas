numbers = [1, 2, 3, 4, 5, 6]

evens = filter(lambda x: x % 2 == 0, numbers)
odds = filter(lambda x: x % 2 != 0, numbers)

dict = {
    "pares": list(evens),
    "impares": list(odds)
}
print(dict)