from functools import reduce

def wordcounter(words):
    
    length = map(len, words)
    return reduce(lambda x, y: x + y, length)

words = ["casa", "python", "lambda"]
print(wordcounter(words))