numbers = [1, -2, 0, 3, -5, 0]

positives = filter(lambda x: x >= 0, numbers)
negatives = filter(lambda x: x < 0, numbers)
zero = filter(lambda x: x == 0, numbers)

dict = {
    "positivos": list(positives),
    "negativos": list(negatives),
    "zeros": list(zero)
}

print(dict)
