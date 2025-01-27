word1=input("Digite a primeira palavra: ")
word2 = input("Digite a segunda palavra: ")

def anagram(p1, p2):
    p1 = p1.replace(" ", "").lower()
    p2 = p2.replace(" ", "").lower()
    return sorted(p1) == sorted(p2)

if anagram(word1, word2):
    print("As palavras escolhidas são anagramas.")
else:
    print("As palavras escolhidas não são anagramas.")
