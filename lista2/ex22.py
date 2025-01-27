vog = ['a', 'e', 'i', 'o', 'u']
frase = input("Digite uma frase: ")
vogs = 0
cons = 0

frasel = frase.replace(" ", "").lower()

for i in frasel:
    if i not in vog:
        cons +=1
    else:
        vogs +=1
        
print(f"A quantidade de vogais é {vogs}, e a quantidade de consoantes é {cons}.")