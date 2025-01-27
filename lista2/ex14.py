word = input("Escreva uma palavra: ")

def palindromos(text):
    text2 = text.lower()
    return text2 == text2[::-1]

if palindromos(word):
    print(f"Sim, a palavra {word} é um palíndromo.")
else:
    print(f"Não, a palavra {word} não é um palíndromo.")