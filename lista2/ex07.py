word = input("Digite uma palavra: ")
fword = ''
aux = -1
for i in word:
    fword += word[aux]
    aux -=1
print(fword)