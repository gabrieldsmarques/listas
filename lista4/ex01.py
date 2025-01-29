def reverter_caracteres(word):
    if len(word) <= 1:
        return word
    else:
        return reverter_caracteres(word[1:]) + word[0]

print(reverter_caracteres("gabriel"))
    