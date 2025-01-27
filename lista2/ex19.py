dic ={}

def counter(frase):
      for char in frase:
            if char in dic:
                  dic[char] +=1
            else:
                  dic[char] = 1
      return dic

word = input("Digite uma frase: ")
result = counter(word)

print(result)


