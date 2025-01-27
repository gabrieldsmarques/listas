word = input("Digite uma palavra: ")
aux = ""

for i in word:
    if i not in aux:
        aux += i

print(len(aux))